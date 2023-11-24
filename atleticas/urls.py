from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_index, name='pagina_index'),
    path('login/', views.pagina_login, name='pagina_login'),
]
