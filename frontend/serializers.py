from rest_framework import serializers
from .models import cachedFile, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class fileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cachedFile
        fields = '__all__'
class userSerializer(serializers.HyperlinkedModelSerializer):
    gdrive_auth = serializers.CharField(source="profile.gdrive_auth")
    class Meta:
        model = User
        exclude = ['password','is_superuser','first_name','last_name']

class registerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
        validated_data['email'], validated_data['password'])
        return user
class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials.")
