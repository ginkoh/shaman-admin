from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.messages, name='messages'),
    path('<str:room_name>/', views.room, name='room'),
]
