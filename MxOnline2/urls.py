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

from user.views import LoginView, RegisterView, ActivateView, ForgetPwdView, ResetPwdView, ModifyPwdView

from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 账户相关urls设置
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^activate/(?P<activation_code>.*)/$', ActivateView.as_view(), name='activate'),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forgetpwd'),
    url(r'^resetpwd/(?P<reset_code>.*)/$', ResetPwdView.as_view(), name='resetpwd'),
    url(r'^modifypwd/$', ModifyPwdView.as_view(), name='modifypwd'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # organization相关url
    url(r'^org/', include('organization.urls',  namespace='org')),

    # course相关url
    url(r'^course/', include('course.urls', namespace='course')),
]

