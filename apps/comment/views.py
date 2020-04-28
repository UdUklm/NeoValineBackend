from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import CommentModel
from .serializers import CommentSerializer


class CommentPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'  # 每页的大小
    page_query_param = 'page'  # 要的是哪一页
    max_page_size = 1000  # 分页上限

    def get_paginated_response(self, data):
        return Response(data)


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    评论
    create: 添加评论
    list: 获取评论列表
    detail: 评论详情
    """
    queryset = CommentModel.objects.filter(display=True, rid=None, pid=None)
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_fields = ['url']
    ordering_fields = ['ctime']


class ReplyViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    获取回复类的评论
    list: 获取评论列表
    detail: 评论详情
    """
    queryset = CommentModel.objects.filter(display=True, rid__isnull=False,
                                           pid__isnull=False)
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_fields = ['url', 'rid', 'pid']
    ordering_fields = ['ctime']
