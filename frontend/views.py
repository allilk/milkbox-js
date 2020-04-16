from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import cachedFile
from .serializers import fileSerializer, userSerializer
import django_filters
# from rest_framework_api_key.permissions import HasAPIKey

def index(request):
    return render(request, 'files.html')
    
class fileFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    users = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    shared_with = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = cachedFile
        fields = '__all__'
        
class fileViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [HasAPIKey]
    queryset = cachedFile.objects.all()
    serializer_class = fileSerializer
    filterset_class = fileFilter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class userViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [HasAPIKey]
    queryset = User.objects.select_related('userprofile').all()
    serializer_class = userSerializer
    filter_backends = [DjangoFilterBackend]

