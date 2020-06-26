"""NeoValineBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.views import serve
from django.urls import path
from django.conf.urls import include
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from apps.comment.views import CommentViewSet
from apps.comment.views import ChildCommentViewSet
from NeoValineBackend.settings import STATIC_ROOT

from django.views import static
from django.conf import settings
from django.conf.urls import url

router = DefaultRouter()
router.register(r'api/comment', CommentViewSet)
router.register(r'api/childcomment', ChildCommentViewSet)


urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # path(r'api/doc/', include_docs_urls(title='API Doc')),
    path(r'api/admin/', xadmin.site.urls),
    path(r'api/static/', serve, {'document_root': STATIC_ROOT}),
    path('', include(router.urls)),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
]
