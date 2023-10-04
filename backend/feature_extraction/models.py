from django.db import models

#テキスト情報を保存する
from django.db import models

class TextInfo(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


    