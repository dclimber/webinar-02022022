from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def home_page(request):
    template_rendered_to_string = render_to_string('home.html')
    return HttpResponse(template_rendered_to_string)
