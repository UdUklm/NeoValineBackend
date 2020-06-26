from rest_framework import serializers
from rest_framework import ISO_8601
from .models import CommentModel


class CommentSerializer(serializers.ModelSerializer):
    notified = serializers.BooleanField(read_only=True)
    display = serializers.BooleanField(read_only=True)
    ctime = serializers.DateTimeField(read_only=True, format=ISO_8601)
    ip = serializers.IPAddressField(write_only=True)

    class Meta:
        model = CommentModel
        fields = '__all__'  # 序列化所有字段
