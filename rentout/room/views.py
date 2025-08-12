from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# 使用django封装好的connection对象，会自动读取settings.py中数据库的配置信息
from django.db import connection
from .models import User

# Create your views here.
def register(request):
    new_user = User(email='parado@163.com',password='123',birthday='1999-11-11',first_name='Para',last_name='Huang',major_city_id=53)
    new_user.save()
    return JsonResponse({'code':200,'msg':'register successfully'})
