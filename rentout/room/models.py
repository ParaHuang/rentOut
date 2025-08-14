from django.db import models

# Create your models here.

class Area(models.Model):
    city = models.CharField(max_length=30,null=False)
    class Meta:
        db_table = 'area'
class User(models.Model):
    email = models.EmailField(unique=True)  # 通常邮箱应该唯一
    password = models.CharField(max_length=128, null=False)  # 密码建议更长
    first_name = models.CharField(max_length=50, null=False)  # Django推荐小写加下划线命名
    last_name = models.CharField(max_length=50, null=False)
    gender = models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')],default=0)  # 添加选择项
    birthday = models.DateField(null=False, blank=True)  # 生日可为空
    is_looking = models.BooleanField(default=False)
    has_house = models.BooleanField(default=False)
    major_city = models.ForeignKey("Area", on_delete=models.RESTRICT, null=False, blank=True)
    class Meta:
        db_table = "user"  # 可选
