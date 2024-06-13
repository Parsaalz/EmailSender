from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
def mainpage(request):
    if request.method=="POST":
        subject_t=request.POST.get('subject')
        Message_t=request.POST.get('Message')
        email_t=request.POST.get('email')
        email_re=request.POST.get('email_re')
        password_t=request.POST.get('password')
        settings.EMAIL_HOST_USER=email_t
        settings.EMAIL_HOST_PASSWORD=password_t
        if Message_t and subject_t is not None:
            # s=["gmail@gmail.com","gmail@gmail.com"]
            s=email_re.split(',')
            for x in s:
                email=EmailMessage(
                    subject_t,
                    Message_t,
                    "gmail@gmail.com",
                    [x],
                ).send()
    return render(request,"mainpage.html")
#'bjgpyykfvowtuuiq'
# rxwgyxsleedddkcg ,wwsgapgnbwzrijgm 