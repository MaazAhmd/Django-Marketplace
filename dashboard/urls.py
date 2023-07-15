from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("edit/<int:pk>", views.edit, name='edit'),
    path("delete/<int:pk>", views.deleteItem, name='delete'),
]
