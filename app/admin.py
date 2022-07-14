from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # makes a list like view in admin panel for admin and users
from app.models import User,post,Report

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(post)
admin.site.register(Report)
