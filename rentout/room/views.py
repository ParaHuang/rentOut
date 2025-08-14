# from django.shortcuts import render,HttpResponse
# from django.http import JsonResponse
# # 使用django封装好的connection对象，会自动读取settings.py中数据库的配置信息
# from django.db import connection
# from .models import User
#
# # Create your views here.
# def register(request):
#     new_user = User(email='parado@163.com',password='123',birthday='1999-11-11',first_name='Para',last_name='Huang',major_city_id=53)
#     new_user.save()
#     return JsonResponse({'code':200,'msg':'register successfully'})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # 验证通过后，序列化器会自动处理密码加密
            serializer.save()
            return Response(
                {'code': 200, 'msg': 'register successfully'},
                status=status.HTTP_201_CREATED
            )
        # 返回详细的错误信息，方便调试
        return Response(
            {
                'code': 400,
                'msg': '注册失败',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UserLoginView(APIView):
    def post(self, request):
        # 1. 获取登录凭据
        email = request.data.get('email')
        password = request.data.get('password')

        # 2. 验证必填字段
        if not email or not password:
            return Response(
                {'error': '邮箱和密码是必填项'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 3. 查找用户
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'error': '用户不存在'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # 4. 验证密码
        if not check_password(password, user.password):
            return Response(
                {'error': '密码错误'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # 5. 返回简单成功响应（不含任何token/session）
        return Response({
            'code': 200,
            'msg': '登录验证成功',
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        }, status=status.HTTP_200_OK)