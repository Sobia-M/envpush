from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email',
    'This is a test email from Django',
    settings.EMAIL_HOST_USER,
    ['sobia5122k@gmail.com'],
    fail_silently=False,
)