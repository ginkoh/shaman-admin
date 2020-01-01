from django.contrib import admin
from .models import Chat, ChatMessage


# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'uuid']


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'message_author', 'created', 'updated', 'editable']


admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
