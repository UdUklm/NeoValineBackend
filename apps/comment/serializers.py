from rest_framework import serializers
from .models import CommentModel


class CommentSerializer(serializers.ModelSerializer):
    notified = serializers.BooleanField(read_only=True)
    display = serializers.BooleanField(read_only=True)
    ctime = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CommentModel
        fields = '__all__'  # 序列化所有字段
