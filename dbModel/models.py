# -*- coding: utf-8 -*-
from django.db import models
from django.db import models

# Create your models here.
# 图片地址列表
class picModel(models.Model):
    # 图片地址
    source = models.CharField(max_length=200) 
    # 图片地址
    thumbnail = models.CharField(max_length=200, default="") 
    # 图片分类
    pic_class = models.IntegerField(default=0)
    # 地址是否有效
    sourceValid = models.BooleanField(default=1)