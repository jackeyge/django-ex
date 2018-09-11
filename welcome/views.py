import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from django.core.cache import cache  # 引入缓存模块
from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count(),
        'message': 'This is a test'
    })

def health(request):
    return HttpResponse("ok")

def redisTest(request):
    cache.set('v', 'This is data from redis', 60 * 60)  # 写入key为v，值为555的缓存，有效期30分钟
    cache.has_key('v')  # 判断key为v是否存在
    return HttpResponse(cache.get('v'))  # 获取key为v的缓存
def metrics(request):
    v = PageView.objects.count()
    return HttpResponse("page_views %s" %v)