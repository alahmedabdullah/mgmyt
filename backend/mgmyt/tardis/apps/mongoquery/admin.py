from django.contrib import admin
from .models import UserCollection, Collection, Job

admin.site.register(UserCollection)
admin.site.register(Collection)
admin.site.register(Job)
