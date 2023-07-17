from django.urls import path

from . import views

urlpatterns = [
    path('<int:item_pk>/', views.conversation, name='conversation'),
    path('', views.inbox, name='inbox'),
    path('chat/<int:pk>', views.chat, name='chat'),
]
