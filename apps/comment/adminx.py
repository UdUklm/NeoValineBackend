from .models import CommentModel
import xadmin


class CommentModelAdmin(object):
    # 定义显示的属性
    list_display = ['id', 'url', 'comment', 'nickname', 'email', 'link',
                    'notified', 'display', 'rid', 'pid', 'ip', 'ua', 'ctime']
    # 定义过滤器用于筛选数据, 注意外键的写法是:外键名__外键的某个属性, 才能正常显示过滤, 注意下划线有两个
    list_filter = ['notified', 'display', 'id', 'url', 'comment', 'nickname',
                   'email', 'link', 'rid', 'pid', 'ip', 'ua', 'ctime']
    # 定义可搜索的范围, 不能设置时间, 涉及外键的时候和上面一样处理
    search_fields = ['id', 'url', 'comment', 'nickname', 'email', 'link', 'rid',
                     'pid', 'ip', 'ua']


xadmin.site.register(CommentModel, CommentModelAdmin)
