from django.contrib import admin
from .models import ChatUser


# Register your models here.
class ChatUserAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'is_operator', 'is_registered', 'created', 'updated', 'uuid']

    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user'
    get_username.short_description = 'username'


admin.site.register(ChatUser, ChatUserAdmin)
