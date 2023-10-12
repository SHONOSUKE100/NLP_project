
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json, nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# json構成の関数
def tree_to_dict(tree):
    """
    Convert an NLTK tree to a dictionary.
    """
    node_label = tree.label() if hasattr(tree, 'label') else None

    # If it's a leaf node (a single tuple), return the tuple
    if isinstance(tree, tuple):
        return {"word": tree[0], "tag": tree[1]}
    else:
        tree_dict = {}
        tree_dict['label'] = node_label
        tree_dict['children'] = [tree_to_dict(child) for child in tree]
        return tree_dict

#　Rule-Base　の　NER関数
def ner_to_json(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    namedEnt = nltk.ne_chunk(tagged, binary=True)
    tree_dict = tree_to_dict(namedEnt)
    return json.dumps(tree_dict, indent=4)

# 仮にメモリ内に結果を保存（本番環境ではデータベース等を使用）
processed_text_memory = ''

@api_view(['POST'])
def process_text(request):
    received_text = request.data.get('text', None)
    
    if received_text is not None:
        processed_text = ner_to_json(received_text)
        
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
