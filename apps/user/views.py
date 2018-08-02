from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse
import json

from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from .models import UserProfile, EmailVerifyRecords
from utils.email_send import send_email_verifycord
from extra_apps.utils.mixin_utils import LoginRequiredMixin
from .forms import HeadshotForm, UpdatePwdForm, UpdateInfoForm
from operation.models import UserCourses, UserFavs, UserMsgs
from organization.models import Organizations, Teachers
from course.models import Courses


class LoginView(View):
    """
    用户登陆
    """
    def get(self, request):
        return render(request, 'login.html')

    def post(self,request):
        login_form = LoginForm(request.POST)
        # 验证登陆表单
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            # 用户验证
            user = authenticate(username=username, password=password)
            # 用户验证通过
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            # 用户验证不通过
            else:
                return render(request, 'login.html', {'login_msg': '用户名或密码错误', 'login_form':login_form})
        # 登陆表单验证失败
        else:
            return render(request, 'login.html', {'login_form':login_form})


class RegisterView(View):
    """
    用户注册
    """
    def get(self, request):
        # 生成验证码
        register_captcha_form = RegisterForm()
        return render(request, 'register.html', {"register_captcha_form":register_captcha_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        # 验证注册表单
        if register_form.is_valid():
            email = request.POST.get('email')
            # 检查邮箱是否已注册
            if UserProfile.objects.filter(email=email):
                register_captcha_form = RegisterForm()
                return render(request, 'register.html', {
                    'register_form':register_form,
                    'register_msg':'该邮箱已被注册',
                    'register_captcha_form':register_captcha_form,
                })

            password = make_password(request.POST.get('password'))
            user = UserProfile()
            user.email = email
            user.username = email
            user.password = password
            user.save()

            # 发送激活邮件
            send_email_verifycord(email=email, send_type='register')
            return render(request, 'login.html', {
                'register_form':register_form,
                'activate_msg':'请查看邮箱激活链接',
            })
        # 注册表单验证不通过
        else:
            register_captcha_form = RegisterForm()
            return render(request, 'register.html', {
                'register_form':register_form,
                'register_captcha_form':register_captcha_form,
            })


class ActivateView(View):
    """
    用户账号激活
    """
    def get(self, request, activation_code):
        # 在数据库中匹配激活码
        db_codes = EmailVerifyRecords.objects.filter(code=activation_code, send_type='register')
        # db有对应激活码，激活用户
        if db_codes:
            email = db_codes[0].email
            user = UserProfile.objects.filter(email=email)
            user = user[0]
            user.is_active = True
            user.save()
            return render(request, 'activate_success.html')
        # 查找不到相关激活码
        else:
            return render(request, 'activate_fail.html')


class ForgetPwdView(View):
    """
    找回密码
    """
    def get(self, request):
        forget_captcha_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html', {'forget_captcha_form':forget_captcha_form})

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email')
            users_set = UserProfile.objects.filter(email=email)
            if users_set:
                user = users_set[0]
                send_email_verifycord(email=user.email, send_type='forget')
                return render(request, 'login.html', {'success_forget':"重置链接已发送到邮箱", 'forget_form':forget_form})
            else:
                forget_captcha_form = ForgetPwdForm()
                return render(request, 'forgetpwd.html', {
                    'unregister_error':'该邮箱未注册',
                    'forget_form':forget_form,
                    'forget_captcha_form': forget_captcha_form,
                })
        else:
            forget_captcha_form = ForgetPwdForm()
            return render(request, 'forgetpwd.html', {
                'forget_form':forget_form,
                'forget_captcha_form':forget_captcha_form,
            })


class ResetPwdView(View):
    """
    重置密码链接
    """
    def get(self, request, reset_code):
        code_records_set = EmailVerifyRecords.objects.filter(code=reset_code, send_type='forget')
        if code_records_set:
            code_record = code_records_set[0]
            email = code_record.email
            return render(request, 'password_reset.html', {'email':email})
        else:
            return render(request, 'reset_fail.html')


class ModifyPwdView(View):
    """
    修改密码页面
    """
    def post(self, request):
        modifypwd_form = ModifyPwdForm(request.POST)
        if modifypwd_form.is_valid():
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                email = request.POST.get('email')
                return render(request, 'password_reset.html', {'msg':'两次密码不一致', 'email':email})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(request.POST.get('password1'))
            user.save()
            return render(request, 'reset_success.html')
        else:
            email = request.POST.get('email')
            return render(request, 'password_reset.html', {
                'modifypwd_form':modifypwd_form,
                'email':email,
            })


# 用户个人中心
# 用户信息
class UserInfoView(LoginRequiredMixin, View):
    """
    个人信息页面展示
    """
    def get(self, request):
        return render(request, 'usercenter-info.html')

    def post(self, request):
        info_form = UpdateInfoForm(request.POST, instance=request.user)
        if info_form.is_valid():
            info_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"failure","msg":"操作失败"}', content_type='application/json')


class UpdateHeadshotView(LoginRequiredMixin, View):
    """
    修改头像
    """
    def post(self, request):
        headshot_form = HeadshotForm(request.POST, request.FILES, instance=request.user)
        if headshot_form.is_valid():
            headshot_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(LoginRequiredMixin, View):
    """
    修改密码xxxxxx
    """
    def post(self, request):
        updatepwd_form = UpdatePwdForm(request.POST)
        if updatepwd_form.is_valid():
            password1 = updatepwd_form.cleaned_data.get('password1')
            password2 = updatepwd_form.cleaned_data.get('password2')
            if password1 != password2:
                return HttpResponse('{"msg":"两次密码不一致"}', content_type='application/json')
            request.user.password = make_password(password2)
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(updatepwd_form.errors), content_type='application/json')


class SendEmailCodeView(LoginRequiredMixin, View):
    """
    修改邮箱-发送邮箱验证码
    """
    def get(self, request):
        email = request.GET.get('email', '')

        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已存在"}', content_type='application/json')

        send_email_verifycord(email=email, send_type='updateemail')
        return HttpResponse('{"status":"success"}', content_type='application/json')


class UpdateEmailView(LoginRequiredMixin, View):
    """
    修改邮箱
    """
    def post(self, request):
        email = request.POST.get('email', '')
        code = request.POST.get('code', '')

        if EmailVerifyRecords.objects.filter(email=email, code=code, send_type='updateemail'):
            request.user.email = email
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')

        return HttpResponse('{"status":"fail"}', content_type='application/json')


class MyCoursesView(LoginRequiredMixin, View):
    """
    我的课程
    """
    def get(self,request):
        user_courses = UserCourses.objects.filter(user=request.user)
        return render(request, 'usercenter-mycourse.html', {"user_courses":user_courses})


class MyFavOrgsView(LoginRequiredMixin, View):
    """
    我的收藏-课程机构
    """
    def get(self,request):
        all_userfavorgs = UserFavs.objects.filter(user=request.user, fav_type=2)
        org_ids = [userfavorg.fav_id for userfavorg in all_userfavorgs]
        org_list = []
        for org_id in org_ids:
            org = Organizations.objects.get(id=org_id)
            org_list.append(org)
        return render(request, 'usercenter-fav-org.html',{
            'org_list':org_list,
        })


class MyFavTeachersView(LoginRequiredMixin, View):
    """
    我的收藏-授课讲师
    """
    def get(self,request):
        all_userfav_teachers = UserFavs.objects.filter(user=request.user, fav_type=3)
        teacher_ids = [fav_teachers.fav_id for fav_teachers in all_userfav_teachers]
        teacher_list = []
        for teacher_id in teacher_ids:
            teacher = Teachers.objects.get(id=teacher_id)
            teacher_list.append(teacher)
        return render(request, 'usercenter-fav-teacher.html',{
            'teacher_list':teacher_list,
        })


class MyFavCoursesView(LoginRequiredMixin, View):
    """
    我的收藏-公开课程
    """
    def get(self,request):
        all_userfav_courses = UserFavs.objects.filter(user=request.user, fav_type=1)
        course_ids = [fav_courses.fav_id for fav_courses in all_userfav_courses]
        course_list = []
        for course_id in course_ids:
            course = Courses.objects.get(id=course_id)
            course_list.append(course)
        return render(request, 'usercenter-fav-course.html',{
            'course_list':course_list,
        })


class MyMessagesView(LoginRequiredMixin, View):
    """
    我的消息
    """
    def get(self,request):
        all_msgs = UserMsgs.objects.filter(user=request.user.id)
        return render(request, 'usercenter-message.html', {
            'all_msgs':all_msgs,
        })