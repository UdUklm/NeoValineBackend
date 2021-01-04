from django.db import models


class CommentModel(models.Model):
    """评论"""
    url = models.CharField(verbose_name='评论页面', max_length=256,
                           help_text='评论页面')
    comment = models.TextField(verbose_name='评论', help_text='评论')
    nick = models.CharField(verbose_name='昵称', blank=True, null=True,
                            max_length=64, help_text='昵称')
    mail = models.EmailField(verbose_name='邮箱', blank=True, null=True,
                             help_text='邮箱')
    link = models.URLField(verbose_name='链接', blank=True, null=True,
                           help_text='链接')
    notified = models.BooleanField(verbose_name='已通知', default=False,
                                   help_text='已通知')
    display = models.BooleanField(verbose_name='能显示', default=False,
                                  help_text='能显示')
    ip = models.GenericIPAddressField(verbose_name='IP', blank=True, null=True,
                                      help_text='IP')
    pid = models.IntegerField(verbose_name='前id', blank=True, null=True,
                              help_text='前id')
    rid = models.IntegerField(verbose_name='根id', blank=True, null=True,
                              help_text='根id')
    ua = models.CharField(verbose_name='UA', max_length=256, blank=True,
                          null=True, help_text='UA')
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True,
                                 help_text='创建时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment
