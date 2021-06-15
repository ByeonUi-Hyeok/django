"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

app_name = 'pybo'
urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path( 'pybo/', include('pybo.urls') ), 
    #pybo\views의 index 함수가 처리하고 리턴해줌 
    # path에 / 넣어주는게 좋다. /붙이면 /붙이지않고 호출해도 장고가 / 붙여준다.

]
