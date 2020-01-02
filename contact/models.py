from django.db import models
import uuid


class ChatUser(models.Model):
    # TODO: Set extra infos from the API values of the user. Such as username in the system, user infos...

    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    # "Is registed on the system".
    is_registered = models.BooleanField(default=False)

    is_operator = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.username

    # def if is operator add more fields?...
