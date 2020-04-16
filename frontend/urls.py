from django.urls import include, path
from rest_framework import routers
from . import views
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('files', views.fileViewSet)
router.register('users', views.userViewSet)

urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', views.registerAPI.as_view()),
    path('auth/login', views.LoginAPI.as_view()),
]

urlpatterns += router.urls


