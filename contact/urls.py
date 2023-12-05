from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('thankyou/', views.thank_you_page, name='thank_you'),
]
