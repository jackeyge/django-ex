import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from django.core.cache import cache  # 引入缓存模块
from . import database
from .models import PageView

import urllib.request

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count(),
        'message': 'This is a test1'
    })

def health(request):
    return HttpResponse("ok")

def redisTest(request):
    #cache.set('w', 'two2', 60 * 60)  # 写入key为v，值为555的缓存，有效期30分钟
    #cache.has_key('w')  # 判断key为v是否存在
    #return HttpResponse(cache.get('w'))  # 获取key为v的缓存
    url = "http://django-psql-example-gxytest-jenkins.swgz.tae.ctyun.cn/redis"
    contents = urllib.request.urlopen(url).read()
    return HttpResponse("get redis value: %s" %contents)


def metrics(request):
    v = PageView.objects.count()
    return HttpResponse("page_views %s" %v)
