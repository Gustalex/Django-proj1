
from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),# Home
    # ter cuidado para passar o tipo do id correto para evitar erros de segurança
    path('recipes/<int:id>/', views.recipe, name="recipe"),# Recipe
]