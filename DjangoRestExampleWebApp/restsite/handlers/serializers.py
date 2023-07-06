from rest_framework import serializers
from .models import Task, TaskStatus

# https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
# The HyperlinkedModelSerializer has the following differences from ModelSerializer:
# It does not include the id field by default.
# It includes a url field, using HyperlinkedIdentityField.
# Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='task-highlight', format='html')

    class Meta:
        model = Task
        fields = ['id', 'title', 'owner', 
                  'created_at', 'status', 
                  'finished_at']

# class TaskSerializer(serializers.ModelSerializer):
#     # If we don't add this line, 'owner' filed will be the user.id
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'owner', 'created_at', 'status', 'finished_at']

# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField(style={'base_template': 'textarea.html'})
#     status = serializers.ChoiceField(choices=[(status.value, status.name) for status in TaskStatus])
#     finished_at = serializers.DateTimeField(allow_null=True, required=False)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Task.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Task` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.status = validated_data.get('status', instance.status)
#         instance.finished_at = validated_data.get('finished_at', instance.finished_at)
#         instance.save()
#         return instance