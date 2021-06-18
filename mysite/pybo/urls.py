from django.urls import path
from . import views
app_name    = 'pybo'
urlpatterns = [
                    path('', views.index, name='index'), 
                    # 이전 urls.py에서 올때 pybo/ 호출되서 옴 그다음 붙을거 넣어줘야함
                    # 공백은 path/ 이걸로 처리하겠다는것
                    # path/로 오면 view.index로 처리한다는 것
                    path('<int:question_id>/', views.detail, name='detail'),
                    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
                    path('question/create/', views.question_create, name='question_create'),
                    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
]