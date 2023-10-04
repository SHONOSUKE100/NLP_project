
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# 仮にメモリ内に結果を保存（本番環境ではデータベース等を使用）
processed_text_memory = ''

@api_view(['POST'])
def process_text(request):
    received_text = request.data.get('text', None)
    
    if received_text is not None:
        processed_text = received_text.upper()
        
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
