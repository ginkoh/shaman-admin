from django.contrib import admin
from .models import Entity


# Register your models here.
class EntityAdmin(admin.ModelAdmin):
    list_display = ['app_name', 'created', 'updated', 'uuid']


admin.site.register(Entity, EntityAdmin)
