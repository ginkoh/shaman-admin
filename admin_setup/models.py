from django.db import models
import uuid


# Create your models here.
class Entity(models.Model):
    app_name = models.CharField(max_length=255)
    # app_key =

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.app_name
