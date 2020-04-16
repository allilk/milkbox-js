from django.contrib import admin
from django.urls import path, include
from frontend.views import index, OAuth2Callback
urlpatterns = [
    path('api/', include('frontend.urls')),
    path('', index),
    path('oauth2callback/', OAuth2Callback),
    path('admin/', admin.site.urls),
]
