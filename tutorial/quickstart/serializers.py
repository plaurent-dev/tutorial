from django.contrib.auth.models import User, Group
from .models import Regex, App, Const, Constants
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RegexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regex
        fields = ['url', 'key', 'value', 'content', 'created_on', 'author']

class ConstSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Const
        fields = ['url','key', 'value']

class ConstantsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Constants
        fields = ['url','key', 'value']

class AppSerializer(serializers.HyperlinkedModelSerializer):
    constants = ConstantsSerializer(many=True, read_only=True)
    regex = RegexSerializer(many=True, read_only=True)
    class Meta:
        model = App
        fields = ['url', 'appname', 'appversion', 'appcontent', 'appcreated_on', 'regex', 'constructeur', 'constants']
