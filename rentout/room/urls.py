from django.urls import path
from . import views

# 指定应用名称（应用命名空间），防止命名冲突
app_name = "room"

urlpatterns = [
    path('register',views.register,name="register")
]