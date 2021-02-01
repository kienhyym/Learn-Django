# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post 
# Create your views here.
from django.http import HttpResponse
def list(request):
    Data = {'Posts':Post.objects.all()}
    return render(request, 'blog.html',Data)