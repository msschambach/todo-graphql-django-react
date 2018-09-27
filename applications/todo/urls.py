from django.urls import path
from applications.todo import views

urlpatterns = [path("", views.home)]
