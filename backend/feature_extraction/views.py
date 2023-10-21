from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json, nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


#　Rule-Base　の　NER関数
import nltk

def rule_based_ner_to_json(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    tree = nltk.ne_chunk(tagged, binary=False)

    entities = []
    nltks = []
    text_modify = []
    for subtree in tree.subtrees():
        if subtree.label() != "S":  # "S"はSentenceのラベルなので除外
            entity_word = " ".join([word for word, tag in subtree.leaves()])
            entities.append({
                "label": subtree.label(),
                "word": entity_word,
            })
        else:
            for leaf in subtree.leaves():

                entities.append({

                    "label": "None",
                    "word": leaf[0],
                })

    for entity in entities:
        if entity["label"] != 'None':
            nltks.append(entity)
    
    for entity in entities:
        flag = False
        if entity["label"] != 'None':
            continue

        for nltk_a in nltks:
            if entity["word"] == nltk_a["word"]:
                text_modify.append(nltk_a)
                flag = True
                break
        if flag!=True:
            text_modify.append(entity)
        
                

    return {
        "text": text_modify,
        "entities": entities,
    }



# 仮にメモリ内に結果を保存（本番環境ではデータベース等を使用）
processed_text_memory = ''

@api_view(['POST'])
def process_text(request):
    received_text = request.data.get('text', None)
    
    if received_text is not None:
        processed_text = rule_based_ner_to_json(received_text)
        
        # 処理結果を保存
        global processed_text_memory
        processed_text_memory = processed_text
        
        return Response({'status': 'processed'}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_processed_text(request):
    global processed_text_memory
    return Response({'result': processed_text_memory}, status=status.HTTP_200_OK)
