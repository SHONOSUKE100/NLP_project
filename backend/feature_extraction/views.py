from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json, nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def rule_based_ner_to_json(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    tree = nltk.ne_chunk(tagged, binary=False)

    nltks = []
    text_modify = []
    
    # Create a dictionary for quick lookup of words found in nltks
    nltks_dict = {}

    for subtree in tree.subtrees():
        if subtree.label() != "S":
            entity_word = " ".join(word for word, tag in subtree.leaves())
            entity_info = {
                "label": subtree.label(),
                "word": entity_word,
            }
            nltks.append(entity_info)
            nltks_dict[entity_word] = entity_info
    
    for leaf in tree.leaves():
        word = leaf[0]
        entity = nltks_dict.get(word, {"label": "None", "word": word})
        text_modify.append(entity)

    return {
        "text": text_modify,
        "entities": nltks + [entity for entity in text_modify if entity['label'] == 'None']
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
