from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from .models import UserProfile, EmailVerifyRecords
from utils.email_send import send_email_verifycord


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
