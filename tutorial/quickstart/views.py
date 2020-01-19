from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Regex, App, Const, Constants
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, RegexSerializer, AppSerializer, ConstSerializer, ConstantsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RegexViewSet(viewsets.ModelViewSet):
    queryset = Regex.objects.all()
    serializer_class = RegexSerializer

class ConstViewSet(viewsets.ModelViewSet):
    queryset = Const.objects.all()
    serializer_class = ConstSerializer

class ConstantsViewSet(viewsets.ModelViewSet):
    queryset = Constants.objects.all()
    serializer_class = ConstantsSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
