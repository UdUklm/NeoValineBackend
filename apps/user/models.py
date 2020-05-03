from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    """
    用户
    """
    email = models.EmailField(verbose_name='邮箱', blank=True, null=True,
                              help_text='邮箱')
    ctime = models.DateTimeField(verbose_name='注册时间', auto_now_add=True,
                                 help_text='注册时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
