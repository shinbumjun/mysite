import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): # 질문 내용, 발행일
    question_text = models.CharField(max_length=200) # 질문 : 문자(200)
    pub_data = models.DateTimeField('date published') # 발행일 : 날짜
    # 원래는 date인데 data로 오타내서 data로 만듬

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1) # 현재시각 - 하루 = 어제 이후에 발행이 된 데이터가 리턴

class Choice(models.Model): # 선택지에 해당하는 질문, 투표수
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # 외래키(Question 데이터 모델을 참조, 1 대 N), Question 기본키가 삭제되면 외래키도 삭제
    choice_text = models.CharField(max_length=200) # 질문 : 문자(200)
    votes = models.IntegerField(default=0) # 투표수 : 숫자

    def __str__(self):
        return self.choice_text