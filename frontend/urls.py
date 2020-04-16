from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('files', views.fileViewSet)
router.register('users', views.userViewSet)

urlpatterns = router.urls


