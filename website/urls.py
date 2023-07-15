from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    path('add/', views.add, name='addItem')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)