from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_atleticas, name='login_atleticas'),
    path('home/', views.home_atleticas, name='home_atleticas'),
]
