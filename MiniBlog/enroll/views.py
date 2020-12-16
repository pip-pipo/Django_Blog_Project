from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponseRedirect
from .models import PostData
from .forms import SignupFrom, LoginForm,PostFrom
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
        if request.method == "POST":
            form = PostFrom(request.POST)
            if form.is_valid():
                titel = form.cleaned_data['titel']
                desc = form.cleaned_data['desc']
                pst = PostFrom(titel=titel,desc=desc)
                pst.save()
                form = PostFrom()
        else:
            form = PostData()
        return render(request,"enroll/templets/blog/addpost.html",{'fm':form})
    else:
        return HttpResponseRedirect('/login/')



# Update post

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = PostData.objects.get(pk=id)
            form = PostFrom(request.POST,isinstance=pi) 
            # problem was ininstance pi (__init__() got an unexpected keyword argument 'isinstance')
            # am was in 2:24m :08s
            if form.is_valid():
                form.save()
        else:
            pi = PostData.objects.get(pk=id)
            form = PostFrom(instance=pi)
        return render(request,"enroll/templets/blog/updatePost.html")
    else:
        return HttpResponseRedirect('/login/')

# delete post

def deletepost(request,id):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dasboard/')
    else:
        return HttpResponseRedirect('/login/')