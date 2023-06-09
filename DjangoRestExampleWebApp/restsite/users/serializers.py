from django.contrib.auth.models import User, Group
from rest_framework import serializers

from handlers.models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'tasks']

# class UserSerializer(serializers.ModelSerializer):
#     tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'tasks']

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
