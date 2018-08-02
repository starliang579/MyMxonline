"""MxOnline2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve

from user.views import LoginView, RegisterView, ActivateView, ForgetPwdView, ResetPwdView, ModifyPwdView, LogoutView
from user.views import IndexView

from .settings import MEDIA_ROOT, STATICFILES_DIRS


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 账户相关urls设置
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^activate/(?P<activation_code>.*)/$', ActivateView.as_view(), name='activate'),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forgetpwd'),
    url(r'^resetpwd/(?P<reset_code>.*)/$', ResetPwdView.as_view(), name='resetpwd'),
    url(r'^modifypwd/$', ModifyPwdView.as_view(), name='modifypwd'),

    # 配置media访问路径
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 配置static访问路径
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATICFILES_DIRS[0]}),

    # organization相关url
    url(r'^org/', include('organization.urls',  namespace='org')),

    # course相关url
    url(r'^course/', include('course.urls', namespace='course')),

    # 用户中心相关urls
    url(r'^users/', include('user.urls', namespace='user')),

]

