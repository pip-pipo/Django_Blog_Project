from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponseRedirect
from .models import PostData
from .forms import SignupFrom, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# home


def home(request):
    posts =PostData.objects.all()
    return render(request, "enroll/templets/blog/home.html" , {'post':posts})
# about


def about(request):
    return render(request, "enroll/templets/blog/about.html")

# contact


def contact(request):
    return render(request, "enroll/templets/blog/contact.html")

# dasboard


def dasboard(request):
    if request.user.is_authenticated:

        posts = PostData.objects.all()

        return render(request, "enroll/templets/blog/dasboard.html",{'post':posts})
    else:
        return HttpResponseRedirect('/login/')
# user login


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "logged in succesfull")
                    return HttpResponseRedirect('/dasboard/')
        else:
            form = LoginForm()
        return render(request, "enroll/templets/blog/login.html", {'form': form})
    else:
        return HttpResponseRedirect('/dasboard/')

# user signup


def user_signup(request):
    if request.method == "POST":
        form = SignupFrom(request.POST)
        if form.is_valid():
            messages.success(
                request, "Congretulation !! You have become an authore")
            form.save()
            form = SignupFrom()

    else:
        print('get request')
        form = SignupFrom()
    return render(request, "enroll/templets/blog/signup.html", {'form': form})

# user logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# add new post

def addnewpost(request):
    if request.user.is_authenticated:
        return render(request,"enroll/templets/blog/addpost.html")
    else:
        return HttpResponseRedirect('/login/')



# Update post

def updatePost(request):
    if request.user.is_authenticated:
        return render(request,"enroll/templets/blog/updatePost.html")
    else:
        return HttpResponseRedirect('/login/')