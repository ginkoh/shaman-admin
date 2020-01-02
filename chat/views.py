import json

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.utils.safestring import mark_safe

from .models import Chat, ChatMessage


# Create your views here.
def index(request):
    chats = Chat.objects.all()
    return render(request, 'chat/index.html', {'chats': chats})


def messages(request):
    messages = list(ChatMessage.objects.all().values('id', 'message', 'message_author', 'editable', 'deletable', 'created', 'uuid'))
    return JsonResponse(messages, safe=False)


def room(request, room_name):
    return HttpResponse(json.dumps({
        'room_name': 'one_room'
    }), content_type='application/json')
    # return render(request, 'chat/room.html', {
    #     # 'room_name_json': mark_safe(json.dumps(room_name))
    #     'room_name_json': 'one_room'
    # })
