from django.contrib import admin

# Register your models here.
from .models import UserProfile,UserInformation

admin.site.register(UserProfile)
admin.site.register(UserInformation)