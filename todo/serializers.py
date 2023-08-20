from rest_framework import serializers
from .models import Todo

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'user',
            'title',
            'description',
            'complete',
            'timestamp'
        )
        read_only_fields = (
            'timestamp',
        )