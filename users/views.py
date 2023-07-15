from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.urls import reverse

from .forms import SignupForm
# Create your views here.

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful.")
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, "Login Failed.")
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def signup(request): 
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/signup.html', {
                'form': form
            })

    form = SignupForm
    return render(request, 'users/signup.html',{
        'form': form
    })