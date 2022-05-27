from django.contrib import admin
from .models import Question, Choice
# Register your models here.

admin.site.register(Question) # 모델중 하나 Question을 admin에 등록
admin.site.register(Choice) # ...