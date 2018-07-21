# _*_ coding:utf-8 _*_
__author__ = 'lqxing'
__date__ = '2018/7/19 10:02'
import random
import string

from django.core.mail import send_mail

from user.models import EmailVerifyRecords


def send_email_verifycord(email, send_type):
    random_code = create_random_code()

    # 注册，发送邮箱激活码
    if send_type == 'register':
        email_subject = '慕学在线网账号激活'
        email_message = '请点击以下链接激活您的慕学在线账号：http://127.0.0.1:8000/activate/{0}/'.format(random_code)

    if send_type == 'forget':
        email_subject = '慕学在线网账号重置密码链接'
        email_message = '请点击以下链接重置您的密码：http://127.0.0.1:8000/resetpwd/{0}/'.format(random_code)

    # 将邮箱验证码保存到数据库
    code_record = EmailVerifyRecords()
    code_record.send_type = send_type
    code_record.email = email
    code_record.code = random_code
    code_record.save()

    # 调用send_email()发送邮件
    send_mail(subject=email_subject, message=email_message, from_email='lqxing1994@sina.com', recipient_list=[email])


def create_random_code(length=16):
    random_code = ''
    all_str = string.ascii_letters + string.digits
    for i in range(length):
        random_code += random.choice(all_str)
    return random_code

