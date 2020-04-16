from django.contrib import admin
from frontend.models import Profile, cachedFile, cachedSharedDrive
# Register your models here.
admin.site.register(Profile)
admin.site.register(cachedFile)
admin.site.register(cachedSharedDrive)