from django.urls import path
from .views import create_todos

urlpatterns = [
    path("todos/", create_todos),
]
