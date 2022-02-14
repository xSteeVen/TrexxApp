"""TREXXAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from . import views
from . import posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^eel/', include('django_eel.urls')), # do not alter this line
    path(r'^TREXXAPP/', include('TREXXAPP.urls')),
    path('', views.index, name='index1'),
    path('index', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('user/login/', views.userLogin, name='userLogin'),
    path('user/login/post', posts.userLogin, name='userLogin_post'),
    path('user/', views.user, name='user'),
    path('user/create/', views.userCreate, name='userCreate'),
    path('user/create/post', posts.userCreate, name='userCreate_post'),
    path('account', views.account, name='account')
]