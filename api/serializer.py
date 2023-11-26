from rest_framework.serializers import Serializer, CharField, DateTimeField, ModelSerializer
from .models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoSerializerForUpdate(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['text', 'expires_at']
