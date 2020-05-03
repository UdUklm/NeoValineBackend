import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate
from email.utils import formataddr

from NeoValineBackend.hidden_options import MAIL_SETTINGS
from NeoValineBackend.hidden_options import SITE_INFO


class MailSender:
    """
    发送新评论提醒邮件
    """

    def __init__(self, subject: str, body: str, service_name: str,
                 receiver_addr: str):
        """
        init 邮件信息
        :param subject: 主题
        :param body: 邮件主体
        :param service_name: 服务名称
        :param receiver_addr: 接收者地址
        """
        self.smtp_host = MAIL_SETTINGS['SMTP_SERVER']
        self.smtp_port = MAIL_SETTINGS['PORT']
        self.ssl_port = MAIL_SETTINGS['SSL_PORT']
        self.sender_addr = MAIL_SETTINGS['ADDRESS']
        self.username = MAIL_SETTINGS['USERNAME']
        self.password = MAIL_SETTINGS['PASSWORD']
        self.subject = subject
        self.body = body
        self.service_name = service_name
        self.receiver_addr = receiver_addr
        self.receiver_name = ''

    def set_receiver_name(self, receiver_name):
        self.receiver_name = receiver_name

    def send(self) -> bool:
        """
        发送邮件
        :return: 邮件发送成功与否
        """
        receivers = [self.receiver_addr]
        encoding = 'utf-8'
        mail = MIMEText(self.body, 'html', encoding)
        mail['Subject'] = Header(self.subject, encoding)
        if self.receiver_name == '':
            self.receiver_name = receivers[0][0:receivers[0].find('@')]
        mail['From'] = formataddr((self.service_name, self.sender_addr))
        mail['To'] = formataddr((self.receiver_name, receivers[0]))
        mail['Date'] = formatdate()

        try:
            smtp = smtplib.SMTP_SSL(self.smtp_host, self.ssl_port)
            smtp.ehlo()
            smtp.login(self.username, self.password)
            smtp.sendmail(self.sender_addr, receivers, mail.as_string())
            smtp.close()
            return True
        except smtplib.SMTPException:
            return False


def mail_admin_notice(post_url: str, nick: str, comment: str) -> bool:
    """
    新评论提醒
    :param comment: 评论内容
    :param nick: 评论者昵称
    :param post_url: 文章 URL
    :return 邮件发送成功与否
    """
    site_name = SITE_INFO['SITE_NAME']
    service_name = '新评论提醒'
    subject = '您的文章有了新的评论'
    body = """
    <div style="border-top:2px solid #12ADDB;box-shadow:0 1px 3px #AAAAAA;
    line-height:180%%;padding:0 15px 12px;margin:50px auto;font-size:12px;">
    <h2 style="border-bottom:1px solid #DDD;font-size:14px;font-weight:normal;
    padding:13px 0 10px 8px;">您在<a style="text-decoration:none;
    color: #12ADDB;" href="%s" target="_blank"> %s </a>上的文章有了新的评论</h2>
    <p><strong>%s </strong>回复说：</p><div style="background-color: #f5f5f5;
    padding: 10px 15px;margin:18px 0;word-wrap:break-word;">%s</div></div>
    """ % (post_url, site_name, nick, comment)
    mail = MailSender(subject, body, service_name, SITE_INFO['ADMIN_MAIL'])
    mail.set_receiver_name(SITE_INFO['ADMIN_NAME'])
    return mail.send()


def mail_display_notice(post_url: str, receiver: str, comment: str) -> bool:
    """
    评论过审提醒
    :param receiver: 接收者
    :param comment: 评论内容
    :param post_url: 文章 URL
    :return 邮件发送成功与否
    """
    site_name = SITE_INFO['SITE_NAME']
    service_name = '评论过审提醒'
    subject = '您在' + site_name + '上的评论过审了'
    body = """
        <div style="border-top:2px solid #12ADDB;box-shadow:0 1px 3px #AAAAAA;
        line-height:180%%;padding:0 15px 12px;margin:50px auto;font-size:12px;">
        <h2 style="border-bottom:1px solid #DDD;font-size:14px;
        font-weight:normal;padding:13px 0 10px 8px;">您在 %s 上的评论过审并显示了</h2>
        <p>评论内容：</p><div style="background-color: #f5f5f5;
        padding: 10px 15px;margin:18px 0;word-wrap:break-word;">%s</div>
        <p>您可以点击<a style="text-decoration:none; color:#12addb" href="%s" 
        target="_blank">博客链接</a>查看您的评论</br></br>
        根据国家相关规定，网站评论需要先审核后显示，感谢您的理解</br>: )</p></div>
        """ % (site_name, comment, post_url)
    mail = MailSender(subject, body, service_name, receiver)
    return mail.send()


def mail_reply_notice(post_url: str, receiver: str, nick: str,
                      comment: str, reply_nick: str, reply_comment: str):
    """
    评论回复提醒
    :param reply_comment: 回复者的评论
    :param reply_nick: 回复者的昵称
    :param nick: 原先评论者的昵称
    :param receiver: 原先评论者的邮箱
    :param comment: 原先评论者的评论内容
    :param post_url: 文章 URL
    :return 邮件发送成功与否
    """
    site_name = SITE_INFO['SITE_NAME']
    service_name = '评论回复提醒'
    subject = '您在' + site_name + '上的评论收到了回复'
    body = """
    <div style="border-top:2px solid #12ADDB;box-shadow:0 1px 3px #AAAAAA;
    line-height:180%%;padding:0 15px 12px;margin:50px auto;font-size:12px;">
    <h2 style="border-bottom:1px solid #DDD;font-size:14px;font-weight:normal;
    padding:13px 0 10px 8px;">您在 %s 上的评论有了新的回复</h2>
    %s 同学，您曾发表评论：<div style="padding:0 12px 0 12px;margin-top:18px">
    <div style="background-color: #f5f5f5;padding: 10px 15px;margin:18px 0;
    word-wrap:break-word;">%s</div><p><strong>%s </strong>回复说：
    </p><div style="background-color: #f5f5f5;padding: 10px 15px;margin:18px 0;
    word-wrap:break-word;">%s</div><p>您可以点击<a style="text-decoration:none; 
    color:#12addb" href="%s" target="_blank">博客链接</a>查看回复的完整內容<br></p></div>
    </br></br>根据国家相关规定，网站评论需要先审核后显示，感谢您的理解</br>: )</p></div>
    """ % (site_name, nick, comment, reply_nick, reply_comment,
           post_url)
    mail = MailSender(subject, body, service_name, receiver)
    return mail.send()
