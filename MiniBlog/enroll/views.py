from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
# from .forms import  SignUpFrom
from .forms import SignupFrom
# Create your views here.


def home(request):
    return render(request, "enroll/templets/blog/home.html")


def about(request):
    return render(request, "enroll/templets/blog/about.html")


def contact(request):
    return render(request, "enroll/templets/blog/contact.html")


def dasboard(request):
    return render(request, "enroll/templets/blog/dasboard.html")


def user_login(request):
    return render(request, "enroll/templets/blog/login.html")


def user_signup(request):
    # form = SignUpFrom()
    # form = UserCreationForm()
    form = SignupFrom()
    return render(request, "enroll/templets/blog/signup.html", {'form': form})


def logout(request):
    return HttpResponseRedirect('/')
