# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
import json
from dbModel.models import picModel
 
# 数据库操作
def feedList(request):
       # 初始化
    response = ""
    response1 = ""
    
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = picModel.objects.all()
        
    
    # 获取单个对象
    # response3 = picSource.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # picSource.objects.order_by('source')[0:2]
    
    #数据排序
    # picSource.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    # picSource.objects.filter(name="runoob").order_by("id")
    
    # 输出所有数据
    # for var in list:
    #     response1 += var.source + " "
    # response = response1
    return HttpResponse(json.dumps(list), content_type="application/json")