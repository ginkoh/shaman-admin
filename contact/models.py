from django.db import models
from company.models import Company
import uuid


class ChatUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    # "Is registered on the system".
    is_registered = models.BooleanField(default=False)
    user_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.username

    # def if is operator add more fields?...
