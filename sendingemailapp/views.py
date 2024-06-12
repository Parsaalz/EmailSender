from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
def mainpage(request):
    if request.method=="POST":
        subject_t=request.POST.get('subject')
        Message_t=request.POST.get('Message')
        if Message_t and subject_t is not None:
            email=EmailMessage(
                subject_t,
                Message_t,
                "parsaalizadeh2022@gmail.com",
                ["parsaalizadeh2040@gmail.com","parsaalizadeh2022@gmail.com"],
            ).send()
    return render(request,"mainpage.html")