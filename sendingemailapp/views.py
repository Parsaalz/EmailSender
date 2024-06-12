from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
def mainpage(request):
    email=EmailMessage(
        "parsa",
        "bye",
        "parsaalizadeh2022@gmail.com",
        ["parsaalizadeh2040@gmail.com","parsaalizadeh2022@gmail.com"],
    ).send()
    return HttpResponse("your email was send")