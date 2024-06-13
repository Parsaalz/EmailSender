from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def login_page(request):
    fr=LoginForm()
    if request.method=="POST":
        fr=LoginForm(data=request.POST)
        if fr.is_valid():
            username_t=fr.cleaned_data.get("username")
            password_t=fr.cleaned_data.get("password")
            user=authenticate(request,username=username_t,password=password_t)
            if user is not None:
                login(request,user)
                return redirect('mainpage')
    context={
        "fr":fr,
    }
    return render(request,"login.html",context)
