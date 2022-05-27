from django.shortcuts import render # 지름길 : render() 함수
from django.http import HttpResponse, HttpResponseRedirect, Http404 # 에러
from django.template import loader
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from django.views import generic

# class기반(제너릭) view 사용하기
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('-pub_data')[:5]
        return Question.objects.filter(
            pub_data__lte=timezone.now()
        ).order_by('-pub_data')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id): # url패턴
    
    # GET, POST방식 설명
    # if request.method == "GET":
    #     do_somthing()
    # elif request.method == "POST":

        question = get_object_or_404(Question, pk=question_id) # 조회

        # return HttpResponse("You're voting on question %s." % question_id)    

        # 설명 : request라는 인자를 받고 HttpResponse 함수를 리턴
        # 클라이언트로부터 request 받게 되면 request 여러가지 정보들이 담겨 있을 것이고 
        # HttpResponse 전에 데이터 추출, 저장, 파일 다운로드 등등을 작성하고
        # HttpResponse 해준다는것만 명심!!! 
        
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice']) # 외래키 조건(tmplates에서 넘겨받은 값을 조회)
        except (KeyError, Choice.DoesNotExist): # 값이 없으면 예외발생
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', { # 데이터가 없는 경우 -> 상세페이지
                'question': question,
                'error_message': "아무것도 투표하지 않았습니다.", # 에러메시지
            })
        else: # 데이터가 있는 경우
            selected_choice.votes += 1 # 선택지에 대한 votes를 1추가 
            selected_choice.save()
            
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # 결과 페이지를 보여줌 


# 함수기반 views
# def index(request): # 정리 : urls.py -> views.py
#     # 1
#     # return HttpResponse("Hello, World.") # 응답

#     # 2
#     # latest_question_list = Question.objects.order_by('-pub_data')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     # Question 데이터 중에서 출판 일자를 정렬해서 5개 까지만 데이터를 가지고오고 ,로 연결

#     # 3
#     # latest_question_list = Question.objects.order_by('-pub_data')[:5]
#     # template = loader.get_template('polls/index.html') # 3. html로 
#     # context = { # 1. context 안에 데이터를 밀어 넣어주고 
#     #     'latest_question_list': latest_question_list, # 2. 데이터를 template에 전달
#     # }
#     # return HttpResponse(template.render(context, request))
    
#     # 4
#     latest_question_list = Question.objects.order_by('-pub_data')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id): # 상세페이지
#     # 1
#     # return HttpResponse("You're looking at question %s." % question_id)

#     # 2
#     try:
#         question = Question.objects.get(pk=question_id) # question_id 전달을 받고 조회를 했을때
#     except Question.DoesNotExist: # 데이터가 없는 경우 에러
#         raise Http404("Question does not exist : 해당 데이터가 없습니다") # text 전달
#     return render(request, 'polls/detail.html', {'question': question})

#     # 3 (이건 이해못함)
#     # def detail(request, question_id):
#     #     question = get_object_or_404(Question, pk=question_id)
#     #     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id): # ...
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})