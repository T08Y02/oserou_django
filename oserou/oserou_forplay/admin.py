from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Result

# Register your models here.
PlayerUser = get_user_model()
admin.site.register(PlayerUser)
admin.site.register(Result)