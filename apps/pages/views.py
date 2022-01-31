from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render


def home_page(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        body = (
            f'Please contact:\n{name}\n{email}\n{phone}'
            f'\nMessage from them:\n{message}'
        )
        send_mail(
            'New message from site',
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.NOTIFICATIONS_EMAIL],
            fail_silently=False,
        )
        return redirect('pages:thank-you')
    return render(request, 'home.html')


def thank_you(request):
    return render(request, 'thank-you.html')
