
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),# Home
    # ter cuidado para passar o tipo do id correto para evitar erros de segurança
    path('recipes/<int:id>/', views.recipe),# Recipe
]