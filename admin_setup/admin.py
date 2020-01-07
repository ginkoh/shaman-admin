from django.contrib import admin
from .models import AdminSetup


# Register your models here.
class AdminSetupAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'uuid']


admin.site.register(AdminSetup, AdminSetupAdmin)
