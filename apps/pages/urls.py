from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('thank-you/', views.thank_you, name='thank-you')
]
