from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    if request.method == 'POST':
        success_msg = ""
        subject = "Website inquiry"
        body = {
            'first_name': request.POST['fname'],
            'last_name': request.POST['lname'],
            'phone': request.POST['phone'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        message = "\n".join(body.values())
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['codercaz8@gmail.com']
        try:
            send_mail(subject, message, email_from, recipient_list)
        except BadHeaderError:
            return HttpResponse('Invalid header found')

        return redirect("home")
    return render(request, "index.html")
