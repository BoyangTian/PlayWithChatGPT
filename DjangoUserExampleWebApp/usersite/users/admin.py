from django.contrib import admin

from .models import AccessKey, Profile

# Register your models here.
admin.site.register(AccessKey)
admin.site.register(Profile)