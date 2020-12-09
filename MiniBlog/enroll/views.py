from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupFrom,LoginForm
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
    form = LoginForm
    return render(request, "enroll/templets/blog/login.html" , {'form':form})


def user_signup(request):
    form = SignupFrom()
    # form = UserCreationForm()
    if request.method == "POST":
        form = SignupFrom(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = SignupFrom()
    return render(request, "enroll/templets/blog/signup.html", {'form': form})


def logout(request):
   
    return HttpResponseRedirect('/')
