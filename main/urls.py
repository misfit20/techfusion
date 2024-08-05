from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Main homepage
    path('account_locked/', views.account_locked, name = 'account_locked')
]