import xadmin

from .models import CommentModel
from apps.utils.mail import mail_display_notice
from apps.utils.mail import mail_reply_notice
from NeoValineBackend.hidden_options import SITE_INFO


class CommentModelAdmin(object):
    # 定义显示的属性
    list_display = ['id', 'url', 'comment', 'nick', 'mail', 'link',
                    'notified', 'display', 'rid', 'pid', 'ctime']
    # 定义过滤器用于筛选数据, 注意外键的写法是:外键名__外键的某个属性, 才能正常显示过滤, 注意下划线有两个
    list_filter = ['notified', 'display', 'id', 'url', 'comment', 'nick',
                   'mail', 'link', 'rid', 'pid', 'ctime']
    # 定义可搜索的范围, 不能设置时间, 涉及外键的时候和上面一样处理
    search_fields = ['id', 'url', 'comment', 'nick', 'mail', 'link', 'rid',
                     'pid']
    readonly_fields = ['id', 'url', 'rid', 'pid']

    def save_models(self):
        """
        检查是否有新的通知需要发邮件，包括：
        1. 过审的评论通知
        2. 新回复的通知
        """
        obj = self.new_obj
        obj.save()
        site_url = SITE_INFO['SITE_URL']

        if obj.display and not obj.notified:
            # 审核通过，但没有通知过
            if obj.mail:
                # 填写了邮箱
                display_notice_ret = \
                    mail_display_notice(post_url=site_url+obj.url,
                                        receiver=obj.mail,
                                        comment=obj.comment)
                if not display_notice_ret:
                    # 邮件未发送成功
                    return
            if obj.pid:
                # 该评论是条回复
                pre = CommentModel.objects.get(id=obj.pid,
                                               url=obj.url,
                                               display=True,
                                               mail__isnull=False)
                reply_notice_ret = \
                    mail_reply_notice(post_url=site_url+pre.url,
                                      receiver=pre.mail,
                                      nick=pre.nick,
                                      comment=pre.comment,
                                      reply_nick=obj.nick,
                                      reply_comment=obj.comment)
                if not reply_notice_ret:
                    return
            obj.notified = True
            obj.save()


xadmin.site.register(CommentModel, CommentModelAdmin)
