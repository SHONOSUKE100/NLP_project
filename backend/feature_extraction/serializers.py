from rest_framework import serializers
from .models import TextInfo

class TextInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextInfo
        fields = ('id', 'text')
