from django.db import models
import uuid
from django.utils import timezone
from contact.models import ChatUser
from admin_setup.models import AdminSetup


class ChatMessage(models.Model):
    message = models.TextField()
    # message_html

    message_author = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='message_author')

    message_status = models.CharField(default='open', max_length=255, choices=[
        ('open', 'open'), ('closed', 'closed'), ('sleep', 'sleep')
    ])

    message_channel = models.CharField(default='chat', max_length=255, choices=[
        ('chat', 'chat'), ('email', 'email')
    ])

    reopen_time = models.DateTimeField(default=None, null=True, blank=True)

    from_operator = models.BooleanField(default=True)

    editable = models.BooleanField(default=False)
    deletable = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.message


# Create your models here.
class ChatConversation(models.Model):
    # The customer and the operators in the conversation.
    # It also can be done dividing operators and customers, but if done, the message has to hold two foreign keys,
    # which one of them will be nullable (or the message is from an operator or from a customer). Said that, i prefer
    # this way.
    # Get operator name and operator profile picture from here.
    # chat_users = models.ManyToManyField(ChatUser, related_name='chat_users', blank=True)
    message_app = models.ForeignKey(AdminSetup, on_delete=models.CASCADE, related_name='message_app')

    operator = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='operator')
    customer = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='customer')

    # All the messages of the chat.
    # Get last message from here. DON'T ACCEPT HTML MESSAGES FROM THE USER, IF IT IS NOT FROM THE EMAIL CHANNEL.
    messages = models.ManyToManyField(ChatMessage, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.customer.username
        # return "{}".format(self.pk)
