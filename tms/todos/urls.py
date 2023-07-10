from django.urls import path

from . import views

urlpatterns = [
    path('/', views.todos, name='todos'),
    path('/create', views.create_todo, name='create'),
]