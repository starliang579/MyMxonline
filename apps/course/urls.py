# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/24 16:02'
from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseLessonView, CourseCommentView, AddCommentView


app_name = 'course'
urlpatterns = [
    url('^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情页面
    url('^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='course_detail'),

    # 开始学习-课程章节页
    url('^lesson/(?P<course_id>\d+)$', CourseLessonView.as_view(), name='course_lesson'),

    # 课程评论页面
    url('^comment/(?P<course_id>\d+)$', CourseCommentView.as_view(), name='course_comment'),

    # 发表评论
    url('^add_comment/$', AddCommentView.as_view(), name='add_comment'),
]