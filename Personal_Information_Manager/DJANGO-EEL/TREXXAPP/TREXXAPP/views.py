from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import django_eel as eel

# Create your views here.
eel.init('TREXXAPP/templates/TREXXAPP')

def index(request):
    return render(request, "templates/TREXXAPP/index.html", {})


def userCreate(request):
    return render(request, "templates/TREXXAPP/register.html")


def user(request):
    return render(request, "templates/TREXXAPP/user.html")


def userLogin(request):
    return render(request, "templates/TREXXAPP/login.html")


def account(request):
    cookie = request.COOKIES.get('hash', 'none')
    if(cookie != 'none'):
        if(User.objects.filter(hash=cookie).exists()):
            user = User.objects.get(hash=cookie)
            return render(request, "templates/TREXXAPP/account.html", user)
    return render(request, "templates/TREXXAPP/login.html")

eel.start('templates/TREXXAPP/index.html', size=(800, 600))