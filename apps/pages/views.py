from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def thank_you(request):
    return render(request, 'thank-you.html')
