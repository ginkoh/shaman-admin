from django.db import models
import uuid
from django.utils import timezone
from contact.models import ChatUser


class ChatMessage(models.Model):
    message = models.TextField()
    message_author = models.ForeignKey(ChatUser, on_delete=models.CASCADE)

    editable = models.BooleanField(default=False)
    deletable = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.message


# Create your models here.
class Chat(models.Model):
    # The customer and the operators in the conversation.
    # It also can be done dividing operators and customers, but if done, the message has to hold two foreign keys,
    # which one of them will be nullable (or the message is from an operator or from a customer). Said that, i prefer
    # this way.
    chat_users = models.ManyToManyField(ChatUser, related_name='chat_users', blank=True)

    # All the messages of the chat.
    messages = models.ManyToManyField(ChatMessage, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.chat_users.first().user.username
        # return "{}".format(self.pk)
