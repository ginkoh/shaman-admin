from django.db import models
import uuid
from django.utils import timezone
from contact.models import ChatUser
from admin_setup.models import Entity


class ChatOperator(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='entity')

    profile_picture = models.ImageField(upload_to='images/users/profile_pictures')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.username


# Create your models here.
class ChatConversation(models.Model):
    message_app = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='message_app')

    operator = models.ForeignKey(ChatOperator, on_delete=models.CASCADE, related_name='operator')
    customer = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='customer')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return 'conversation_from_' + self.operator.username + '_and_' + self.customer.username
        # return "{}".format(self.pk)


class ChatMessage(models.Model):
    message_author = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='message_author')
    message_conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE, related_name='message_conversation')
    message_content = models.TextField()
    # message_html

    message_status = models.CharField(default='open', max_length=255, choices=[
        ('open', 'open'), ('closed', 'closed'), ('sleep', 'sleep')
    ])
    message_channel = models.CharField(default='chat', max_length=255, choices=[
        ('chat', 'chat'), ('email', 'email')
    ])

    from_operator = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)
    deletable = models.BooleanField(default=False)

    reopen_time = models.DateTimeField(default=None, null=True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.message_content
