from django.urls import path
from . import views

urlpatterns = [
    # Get a single conversation object by her uuid.
    path('conversation/<str:admin_app_uuid>/<str:conversation_uuid>/', views.conversation, name='single_conversation'),

    # Get all conversation objects from an user uuid.
    path('conversations/<str:admin_app_uuid>/<str:user_uuid>/', views.conversations_from_user, name='conversations_by_user'),

    # path('conversation/', include('rest_framework.urls'), namespace='rest_framework'),

    path('<str:room_name>/', views.room, name='room'),
]
