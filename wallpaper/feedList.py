# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.core import serializers
from dbModel.models import picModel

from . import picModelEncoder
 
# 数据库操作
def feedList(request):
    print("hahahahah")
    list = picModel.objects.all()
    data = serializers.serialize("json", list, cls=picModelEncoder.picModelEncoder)
    return HttpResponse(data, content_type="application/json")