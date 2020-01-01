from django.shortcuts import render
from .models import Chat


# Create your views here.
def index(request):
    chats = Chat.objects.all()
    return render(request, 'chat/index.html', {'chats': chats})
