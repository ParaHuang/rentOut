from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    major_city = AreaSerializer(read_only=True)
    major_city_id = serializers.IntegerField(write_only=True)

    # 显式定义password字段，确保必填和正确加密
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},  # 在API文档中显示为密码输入框
        min_length=6,  # 设置最小长度
        error_messages={
            'required': '密码是必填项',
            'min_length': '密码长度不能少于6个字符'
        }
    )

    class Meta:
        model = User
        fields = [
            'id', 'email', 'password', 'first_name',
            'last_name', 'gender', 'birthday',
            'is_looking', 'has_house', 'major_city', 'major_city_id'
        ]

    def create(self, validated_data):
        # 加密密码后再保存
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # 更新时也加密密码
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

'''
    # 在serializers.py中添加
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("密码长度至少为8个字符")
        # 可以添加更多复杂度检查
        return value
'''