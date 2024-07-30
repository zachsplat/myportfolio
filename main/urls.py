# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    # Add other paths as needed
]

