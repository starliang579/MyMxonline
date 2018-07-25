from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Organizations, Cities
from operation.models import UserFavs
from .forms import UserAskForm


class OrgListView(View):
    """
    机构列表
    """
    def get(self, request):
        # 获取所有机构
        all_orgs = Organizations.objects.all()
        # 获取所有城市
        all_cities = Cities.objects.all()

        # 对机构进行筛选：机构类型
        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 对机构进行筛选：城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对机构进行排序：学习人数
        sort = request.GET.get('sort','')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        if sort == 'courses':
            all_orgs = all_orgs.order_by('-course_nums')

        # 机构排名
        hot_orgs = all_orgs.order_by('-students')[:3]

        # 获取符合条件机构的数量
        orgs_count = all_orgs.count()

        # 获取当前页面所在app
        current_app = 'org'

        return render(request, 'org-list.html', {
            'all_orgs':all_orgs,
            'all_cities':all_cities,
            'orgs_count':orgs_count,
            'category':category,
            'city_id':city_id,
            'sort':sort,
            'hot_orgs':hot_orgs,
            'current_app':current_app,
        })


class AddUserAskView(View):
    """
    机构列表页--我要咨询
    """
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse('{"status":"success"', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"提交失败"}', content_type='application/json')


class OrgHomeView(View):
    """
    机构详情--机构首页
    """
    def get(self, request, org_id):
        org = Organizations.objects.get(id=int(org_id))
        current_page = 'org_home'

        # 判断用户是否已收藏机构
        has_fav = False
        if request.user.is_authenticated:
            if UserFavs.objects.filter(user=request.user, fav_type=2, fav_id=org.id):
                has_fav = True

        return render(request, 'org-detail-homepage.html', {
            'org':org,
            'current_page':current_page,
            'has_fav':has_fav,
        })


class OrgCoursesView(View):
    """
    机构详情--机构课程
    """
    def get(self, request, org_id):
        current_page = 'org_courses'
        org = Organizations.objects.get(id=int(org_id))
        all_courses = org.courses_set.all()

        # 判断用户是否已收藏机构
        has_fav = False
        if request.user.is_authenticated:
            if UserFavs.objects.filter(user=request.user, fav_type=2, fav_id=org.id):
                has_fav = True

        return render(request, 'org-detail-course.html', {
            'all_courses':all_courses,
            'current_page': current_page,
            'org': org,
            'has_fav': has_fav,
        })


class OrgDescView(View):
    """
    机构详情--机构介绍
    """
    def get(self, request, org_id):
        current_page = 'org_desc'
        org = Organizations.objects.get(id=int(org_id))

        # 判断用户是否已收藏机构
        has_fav = False
        if request.user.is_authenticated:
            if UserFavs.objects.filter(user=request.user, fav_type=2, fav_id=org.id):
                has_fav = True

        return render(request, 'org-detail-desc.html', {
            'current_page': current_page,
            'org': org,
            'has_fav': has_fav,
        })


class OrgTeachersView(View):
    """
    机构详情--机构讲师
    """
    def get(self, request, org_id):
        current_page = 'org_teachers'
        org = Organizations.objects.get(id=int(org_id))
        all_teachers = org.teachers_set.all()

        # 判断用户是否已收藏机构
        has_fav = False
        if request.user.is_authenticated:
            if UserFavs.objects.filter(user=request.user, fav_type=2, fav_id=org.id):
                has_fav = True

        return render(request, 'org-detail-teachers.html', {
            'current_page': current_page,
            'org': org,
            'all_teachers':all_teachers,
            'has_fav': has_fav,
        })


class AddFavView(View):
    """
    收藏机构（课程、教师）功能
    """
    def post(self,request):
        if  not request.user.is_authenticated:
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', 'json/application')

        fav_id = request.POST.get('fav_id')
        fav_type = request.POST.get('fav_type')
        fav_record = UserFavs.objects.filter(user=request.user, fav_type=int(fav_type), fav_id=(fav_id))
        # 取消收藏
        if fav_record:
            fav_record.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', 'json/application')
        else:
            fav_record = UserFavs()
            fav_record.user = request.user
            fav_record.fav_id = int(fav_id)
            fav_record.fav_type = int(fav_type)
            fav_record.save()
            return HttpResponse('{"status":"success","msg":"已收藏"}', 'json/application')

