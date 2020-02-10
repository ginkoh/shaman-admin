from django.db import models
from admin_setup.models import Entity
import uuid


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=255)

    company_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='company_entity')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.company_name
