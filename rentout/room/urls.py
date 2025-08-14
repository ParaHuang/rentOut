from django.urls import path
from .views import *

# 指定应用名称（应用命名空间），防止命名冲突
app_name = "room"

urlpatterns = [
    path('register',UserRegisterView.as_view(),name="register"),
    path('login',UserLoginView.as_view(),name="login"),
]