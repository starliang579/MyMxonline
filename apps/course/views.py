from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.db.models import Q

from .models import Courses, Resources
from operation.models import UserFavs, UserCourses, Comments


class CourseListView(View):
    """
    课程列表页
    """
    def get(self, request):
        # 获取所有课程
        all_courses = Courses.objects.all().order_by('-add_times')

        # 课程全局搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        sort = request.GET.get('sort', '')
        # 按人气排序
        if sort == 'hot':
            all_courses = all_courses.order_by('-click_nums')
        # 按学习人数排序
        if sort == 'students':
            all_courses = all_courses.order_by('-students')

        # 热门课程推荐
        hot_courses = all_courses.order_by('-click_nums')[:3]

        return render(request, 'course-list.html', {
            'all_courses':all_courses,
            'sort':sort,
            'hot_courses':hot_courses,
            'search_keywords':search_keywords,
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        # 获取当前课程
        course = Courses.objects.get(id=course_id)

        # 获取学习该门课程的用户
        relate_usercourses = course.usercourses_set.all()
        relate_usercourses = relate_usercourses.all()[:5]

        # 相关课程推荐
        relate_courses = Courses.objects.filter(tag=course.tag)[:3]

        # 检查是否有相关收藏
        has_course_fav = False
        has_org_fav = False
        if request.user.is_authenticated:
            # 是否有课程收藏
            if UserFavs.objects.filter(user=request.user, fav_type=1, fav_id=course.id):
                has_course_fav = True
            # 是否有机构收藏
            if UserFavs.objects.filter(user=request.user, fav_type=2, fav_id=course.org.id):
                has_org_fav = True

        # 课程点击数+1
        course.click_nums += 1
        course.save()

        return render(request, 'course-detail.html', {
            'course':course,
            'relate_usercourses':relate_usercourses,
            'relate_courses':relate_courses,
            'has_course_fav':has_course_fav,
            'has_org_fav':has_org_fav,
        })


class CourseLessonView(View):
    """
    课程章节
    """
    def get(self, request, course_id):
        # 获取当前课程
        course = Courses.objects.get(id=course_id)

        # 课程资料
        all_resources = Resources.objects.filter(course=course_id)

        # 学过该课的同学还学过的其它课程
        relate_usercourses = UserCourses.objects.filter(course=course)
        relate_users = [ usercourse.user for usercourse in relate_usercourses ]
        relate_usercourses = UserCourses.objects.filter(user__in=relate_users)
        relate_course_ids = set([ usercourse.course.id for usercourse in relate_usercourses ])
        relate_courses = Courses.objects.filter(id__in=relate_course_ids).order_by('-click_nums')[:3]

        # 将用户与课程关联起来
        if not UserCourses.objects.filter(user=request.user, course=course):
            user_course = UserCourses()
            user_course.user = request.user
            user_course.course = course
            user_course.save()

        return render(request, 'course-video.html', {
            'course':course,
            'all_resources':all_resources,
            'relate_courses':relate_courses,
        })


class CourseCommentView(View):
    """
    课程评论
    """
    def get(self, request, course_id):
        # 获取当前课程
        course = Courses.objects.get(id=course_id)

        # 课程资料
        all_resources = Resources.objects.filter(course=course_id)

        # 学过该课的同学还学过的其它课程
        relate_usercourses = UserCourses.objects.filter(course=course)
        relate_users = [usercourse.user for usercourse in relate_usercourses]
        relate_usercourses = UserCourses.objects.filter(user__in=relate_users)
        relate_course_ids = set([usercourse.course.id for usercourse in relate_usercourses])
        relate_courses = Courses.objects.filter(id__in=relate_course_ids).order_by('-click_nums')[:5]

        # 课程评论
        all_comments = Comments.objects.filter(course=course).order_by('-add_time')

        return render(request, 'course-comment.html', {
            'course': course,
            'all_resources': all_resources,
            'relate_courses': relate_courses,
            'all_comments':all_comments,
        })


class AddCommentView(View):
    """
    增加评论
    """
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', 'json/application')

        course_id = request.POST.get('course_id')
        comment = request.POST.get('comments')

        usercomment = Comments()
        usercomment.user = request.user
        usercomment.course_id = course_id
        usercomment.comment = comment
        usercomment.save()

        return HttpResponse('{"status":"success"}', 'json/application')

