from apps.utils.mail import mail_display_notice
from apps.utils.mail import mail_reply_notice
from apps.utils.mail import mail_daily_hello
from apps.comment.models import CommentModel
from NeoValineBackend.hidden_options import SITE_INFO


def check_notice():
    """
    检查是否有新的通知需要发邮件，包括：
    1. 过审的评论通知
    2. 新回复的通知
    """
    site_url = SITE_INFO['SITE_URL']
    new_display = CommentModel.objects.filter(notified=False, display=True,
                                              mail__isnull=False)
    new_display.len()
    for item in new_display:
        if mail_display_notice(post_url=site_url+item.url, receiver=item.mail,
                               comment=item.comment):
            if item.pid:
                p = new_display.get(id=item.pid, mail__isnull=False)
                if not mail_reply_notice(post_url=site_url+p.url,
                                         receiver=p.mail, nick=p.nick,
                                         comment=p.comment,
                                         reply_nick=item.nick,
                                         reply_comment=item.comment):
                    return
            item.notified = True
            item.save()


def daily_hello():
    """
    站长每日问好
    """
    mail_daily_hello()
