#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import GalleryPhoto, CourseDesc, Post

def index2(request):
    return render(request, 'index2.html', {})

def base(request):
    return render(request, 'base.html', {})

def about(request):
    return render(request, 'about.html', {})

def achievement(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request, 'achievement.html', {'post':post})

def post(request, pk):
    p = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'p':p})

def contact(request):
    return render(request, 'contact.html', {})

def courses(request):
    return render(request, 'courses.html', {})

def toeic(request):
    pretoeic = CourseDesc.objects.get(course_name = 'Pre-TOEIC')
    #toeica = CourseDesc.objects.get(course_name = 'TOEIC A (550+)')
    #toeicb = CourseDesc.objects.get(course_name = 'TOEIC B (650+)')
    #toeichacker = CourseDesc.objects.get(course_name = 'TOEIC Hacker')
    #return render(request, 'toeic.html', {'pretoeic':pretoeic,'toeica':toeica,'toeicb':toeicb,'toeichacker':toeichacker})
    return render(request, 'toeic.html', {'pretoeic':pretoeic})

def vstep(request):
    preb1 = CourseDesc.objects.get(course_name = 'Pre B1 (AVCB)')
    b1 = CourseDesc.objects.get(course_name = 'Level B1')
    return render(request, 'vstep.html', {'preb1':preb1, 'b1':b1})

def giaotiep(request):
    gtcb = CourseDesc.objects.get(course_name = 'Giao tiếp cơ bản')
    gttc = CourseDesc.objects.get(course_name = 'Giao tiếp trung cấp')
    return render(request, 'giao-tiep.html', {'gtcb':gtcb, 'gttc':gttc})

def ielts(request):
    return render(request, 'ielts.html', {})

def gallery(request):
    gallery_photo = GalleryPhoto.objects.all().order_by('-created_at')
    return render(request, 'gallery.html', {'gallery_photo': gallery_photo})
    #return render(request, 'gallery.html', {})

def img(request, pk):
    gallery_photo = GalleryPhoto.objects.all()
    return render(request, 'img.html', {'gallery_photo':gallery_photo})
