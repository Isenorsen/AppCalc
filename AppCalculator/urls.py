from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PartsView),
    path('', views.email),
    path('email.html', views.email, name='email'),
    path('thanks/', views.thanks, name='thanks'),
    path('feedback.html', views.thanks)
]