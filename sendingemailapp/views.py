from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
password=["bjgpyykfvowtuuiq",]
emailname=""
def mainpage(request):
    if request.method=="POST":
        subject_t=request.POST.get('subject')
        Message_t=request.POST.get('Message')
        email_t=request.POST.get('email')
        password_t=request.POST.get('password')
        password.append(password_t)
        if Message_t and subject_t is not None:
            s=["parsaalizadeh2040@gmail.com","parsaalizadeh202@gmail.com"]
            for x in s:
                email=EmailMessage(
                    subject_t,
                    Message_t,
                    "parsaalizadeh2040@gmail.com",
                    [x],
                ).send()
    return render(request,"mainpage.html")


def email_name():
    return "parsaalizadeh2040@gmail.com"

def get_password():
    print(password[0])
    return str(password[0])

get_password()
#'bjgpyykfvowtuuiq '