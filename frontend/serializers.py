from rest_framework import serializers
from .models import cachedFile
from django.contrib.auth.models import User

class fileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cachedFile
        fields = '__all__'

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ['password','is_superuser','first_name','last_name']

