from xadmin import views

import xadmin


# class BaseSetting(object):
#     """使用主题功能"""
#     enable_themes = True
#     use_bootswatch = True
#
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """设置标题和页脚"""
    site_title = "OMS 后台管理系统"
    site_footer = "OMS"
    # menu_style = "accordion"  # 使左侧菜单列表为伸缩样式


xadmin.site.register(views.CommAdminView, GlobalSettings)
