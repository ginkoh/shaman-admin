import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import ChatConversation, ChatMessage
from .functions import limit_number
from contact.models import ChatUser
from .functions import serialize_foreign_key


def messages_from_operator(request, operator_uuid):
    pass
