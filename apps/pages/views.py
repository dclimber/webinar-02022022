from django.shortcuts import redirect, render


def home_page(request):
    if request.method == 'POST':
        return redirect('pages:thank-you')
    return render(request, 'home.html')


def thank_you(request):
    return render(request, 'thank-you.html')
