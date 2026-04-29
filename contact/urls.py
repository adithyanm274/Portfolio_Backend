# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.contact_view, name='contact_send'),
]