from django.contrib import admin
from .models import ChatConversation, ChatMessage, ChatOperator


# Register your models here.
class ChatConversationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created', 'updated', 'uuid']


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['message_author', 'created', 'updated', 'editable', 'uuid']


class ChatOperatorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created', 'updated', 'uuid']


admin.site.register(ChatConversation, ChatConversationAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(ChatOperator, ChatOperatorAdmin)
