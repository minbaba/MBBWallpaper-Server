# -*- coding: utf-8 -*-
 
# from django.http import HttpResponse
from dbModel.models import picModel
from django.core.serializers.json import Serializer

from . import customEncoder, customResponse
 
# 数据库操作
def feedList(request):
    list = picModel.objects.all()
    
    data = customEncoder.CustomEncoder().serialize(list)
    return customResponse.CustomResponse(data, content_type="application/json")