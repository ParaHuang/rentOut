from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def add(request):
    return JsonResponse({'data':'添加成功'})
