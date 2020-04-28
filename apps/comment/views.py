from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import CommentModel
from .serializers import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    评论
    create: 添加评论
    list: 获取评论列表
    detail: 评论详情
        """
    queryset = CommentModel.objects.filter(display=True)  # 查询集过滤
    serializer_class = CommentSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_fields = ['url', 'pid', 'rid']
    ordering_fields = ['ctime']
