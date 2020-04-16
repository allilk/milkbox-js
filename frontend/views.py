import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken

from .models import cachedFile, Profile
from .config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, AUTH_BASE_URL, TOKEN_URL, SCOPES, DEBUG
from .serializers import fileSerializer, userSerializer, registerSerializer, loginSerializer
from requests_oauthlib import OAuth2Session

def index(request):
    print(request.user)
    return render(request, 'files.html')
def OAuth2Callback(request):
    gdrive=OAuth2Session(CLIENT_ID,scope=SCOPES,redirect_uri=REDIRECT_URI)
    auth_url, state=gdrive.authorization_url(
        AUTH_BASE_URL, access_type="offline", prompt="consent")
    if (request.GET.get('code') != None):
        auth_code=request.GET['code']
        token=gdrive.fetch_token(TOKEN_URL,client_secret=CLIENT_SECRET,code=auth_code)
        gdrive=OAuth2Session(token=token)
        user=(gdrive.get('https://www.googleapis.com/drive/v3/about?fields=*')).json()['user']
        display_name=(user['displayName']).replace(' ', '_')
        email_address=user['emailAddress']
        return redirect('#/')
    else: return redirect(auth_url)

class fileFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    users = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    shared_with = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = cachedFile
        fields = '__all__'
        
class fileViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = cachedFile.objects.all().filter()
    serializer_class = fileSerializer
    filterset_class = fileFilter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class userViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
    filter_backends = [DjangoFilterBackend]

class registerAPI(generics.GenericAPIView):
    serializer_class = registerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
class LoginAPI(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })