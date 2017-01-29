#!/usr/bin/env python
# coding=utf-8
import xadmin
from blog.models import Blog

xadmin.site.register(Blog)
