from django.urls import path

from . import views

app_name = 'polls' # 이름명시
urlpatterns = [
    # ex: /polls/ -> index (클라이언트가 polls라고 호출을 하게 되면 패턴대로 아무것도 없으니까 views.index라는 views를 호출)
    # path('', views.index, name='index'), # 함수기반 
    path('', views.IndexView.as_view(), name='index'), # class기반 view 사용

    # ex: /polls/5/ : 상세페이지를 클라이언트에 전달 
    # path('<int:question_id>/', views.detail, name='detail'), 
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/ : url패턴
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # pk란? DB내의 하나의 열, 하나의 데이터를 구분할 수 있는 값, pk값은 중복x
]
