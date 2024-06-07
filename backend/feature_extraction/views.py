from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json, nltk, joblib

### NLTKによる固有表現
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def rule_based_ner_to_json(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    tree = nltk.ne_chunk(tagged, binary=False)

    text_modify = []
    
    for leaf in tree:
        if isinstance(leaf, nltk.Tree):
            entity_word = " ".join(word for word, tag in leaf.leaves())
            entity_info = {
                "label": leaf.label(),
                "word": entity_word,
            }
            text_modify.append(entity_info)
        else:
            text_modify.append({"label": "None", "word": leaf[0]})

    return {
        "text": text_modify,
        "entities": [entity for entity in text_modify if entity['label'] != 'None']
    }

### CRFによる固有表現
# CRF関数を作る
def ner_with_crf(text, model_path):
    # Split the text into sentences
    sentences = nltk.sent_tokenize(text)

    labels = {'"': 0, "''": 1, '#': 2, '$': 3, '(': 4, ')': 5, ',': 6, '.': 7, ':': 8, '``': 9, 'CC': 10, 'CD': 11, 'DT': 12,
    'EX': 13, 'FW': 14, 'IN': 15, 'JJ': 16, 'JJR': 17, 'JJS': 18, 'LS': 19, 'MD': 20, 'NN': 21, 'NNP': 22, 'NNPS': 23,
    'NNS': 24, 'NN|SYM': 25, 'PDT': 26, 'POS': 27, 'PRP': 28, 'PRP$': 29, 'RB': 30, 'RBR': 31, 'RBS': 32, 'RP': 33,
    'SYM': 34, 'TO': 35, 'UH': 36, 'VB': 37, 'VBD': 38, 'VBG': 39, 'VBN': 40, 'VBP': 41, 'VBZ': 42, 'WDT': 43,
    'WP': 44, 'WP$': 45, 'WRB': 46}

    # A list to hold the tokenized and tagged sentences
    tokenized_sentences = []

    # Tokenize and tag each sentence
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        pos_tags = nltk.pos_tag(words)
        mapped_pos_tags = [labels.get(tag) for _, tag in pos_tags]
        input_data = [(word, str(pos_tag)) for word, pos_tag in zip(words, mapped_pos_tags)]
        tokenized_sentences.append(input_data)

    def word2features(sent, i):
        word, pos_tag = sent[i]
        pos_tag = str(pos_tag)
        features = {
            'bias': 1.0,
            'word.lower()': word.lower(),
            'word[-3:]': word[-3:],
            'word[-2:]': word[-2:],
            'word.isupper()': word.isupper(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
            'postag': pos_tag,
            'postag[:2]': pos_tag[:2],
        }
        if i > 0:
            word1, pos_tag1 = sent[i-1]
            pos_tag1 = str(pos_tag1)
            features.update({
                '-1:word.lower()': word1.lower(),
                '-1:word.istitle()': word1.istitle(),
                '-1:word.isupper()': word1.isupper(),
                '-1:postag': pos_tag1,
                '-1:postag[:2]': pos_tag1[:2],
            })
        else:
            features['BOS'] = True

        if i < len(sent)-1:
            word1, pos_tag1 = sent[i+1]
            pos_tag1 = str(pos_tag1)
            features.update({
                '+1:word.lower()': word1.lower(),
                '+1:word.istitle()': word1.istitle(),
                '+1:word.isupper()': word1.isupper(),
                '+1:postag': pos_tag1,
                '+1:postag[:2]': pos_tag1[:2],
            })
        else:
            features['EOS'] = True

        return features


    def sent2features(sent):
        return [word2features(sent, i) for i in range(len(sent))]
    
    processed_text = [sent2features(s) for s in tokenized_sentences]

    crf = joblib.load(model_path)

    ner_pred = crf.predict(processed_text)
    reference_num_to_nertag = {
        '0': 'None',
        '1': 'B-PER',
        '2': 'I-PER',
        '3': 'B-ORG',
        '4': 'I-ORG',
        '5': 'B-LOC',
        '6': 'I-LOC',
        '7': 'B-MISC',
        '8': 'I-MISC'
    }
    changed_ner_pred = [{"label":reference_num_to_nertag.get(str(tag)), "word":word[0]} for tag, word in zip(ner_pred[0], tokenized_sentences[0])]
    return {'text':changed_ner_pred, 'entities':[entity for entity in changed_ner_pred if entity['label'] != 'None']}


# 仮にメモリ内に結果を保存（本番環境ではデータベース等を使用）
processed_text_memory = {'rulebase': '', 'crf': ''}

@api_view(['POST'])
def process_with_rulebase_text(request):
    received_text = request.data.get('text', None)
    
    if received_text is not None:
        processed_text = rule_based_ner_to_json(received_text)
        
        # 処理結果を保存
        processed_text_memory['rulebase'] = processed_text
        
        return Response({'status': 'processed'}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_processed_with_rulebase_text(request):
    return Response({'result': processed_text_memory['rulebase']}, status=status.HTTP_200_OK)

@api_view(['POST'])
def process_with_crf_text(request):
    received_text = request.data.get('text', None)
    
    if received_text is not None:
        processed_text = ner_with_crf(received_text, "./nlp_model/optimal_crf_model.pkl")
        
        # 処理結果を保存
        processed_text_memory['crf'] = processed_text
        
        return Response({'status': 'processed'}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_processed_with_crf_text(request):
    return Response({'result': processed_text_memory['crf']}, status=status.HTTP_200_OK)
