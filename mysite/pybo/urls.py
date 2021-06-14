from django.urls import path
from . import views

urlpatterns = [
                    path('', views.index) 
                    # 이전 urls.py에서 올때 pybo/ 호출되서 옴 그다음 붙을거 넣어줘야함
                    # 공백은 path/ 이걸로 처리하겠다는것
                    # path/로 오면 view.index로 처리한다는 것
]