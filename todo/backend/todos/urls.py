from .views import ListTodo, DetailTodo
from django.urls import path

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view())

]