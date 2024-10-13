# service/admin.py
from django.contrib import admin
from .models import ServiceRequest, Account, Notification, Comment

admin.site.register(ServiceRequest)
admin.site.register(Account)
admin.site.register(Notification)
admin.site.register(Comment)
