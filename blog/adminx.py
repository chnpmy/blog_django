#!/usr/bin/env python
# coding=utf-8
import xadmin
from blog.models import BlogModel

xadmin.site.register(BlogModel)
