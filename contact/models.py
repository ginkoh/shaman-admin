from django.db import models
from django.contrib.auth.models import User
import uuid


class ChatUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_registered = models.BooleanField(default=False)

    is_operator = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username

    # def if is operator add more fields?...
