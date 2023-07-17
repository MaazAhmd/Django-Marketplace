from django.contrib import admin

# Register your models here.
from .models import Message, Conversation

admin.site.register(Conversation)
admin.site.register(Message)