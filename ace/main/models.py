from django.db import models
from django.contrib.auth.models import User
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print ('a')
print (BASE_DIR)
print ('b')
def get_image_path(instance, filename):
    return os.path.join(BASE_DIR,'static/img/hinh-anh-lop-hoc', str(instance.id), filename)

class Course(models.Model):
    cName = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cName


class CourseDesc(models.Model):
    course = models.ForeignKey(Course, related_name='description')
    course_name = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    duration = models.CharField(max_length=255)
    days_per_week = models.CharField(max_length=255)
    hours_per_day = models.CharField(max_length=255)
    fee = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name

class Post(models.Model):
    title = models.CharField(max_length=255)
    cert = models.ImageField(upload_to='thanh-tich', blank=True, null=True, height_field=None, width_field=None, max_length=100, )
    img = models.ImageField(upload_to='thanh-tich', blank=True, null=True, height_field=None, width_field=None, max_length=100, )
    review = models.ImageField(upload_to='thanh-tich', blank=True, null=True, height_field=None, width_field=None, max_length=100, )
    content = models.CharField(max_length=4000)
    category = models.ForeignKey(Course, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    #created_by = models.ForeignKey(User, related_name='posts')
    #updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        return self.title

class GalleryPhoto(models.Model):
    class_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='hinh-anh-lop-hoc/', blank=True, null=True, height_field=None, width_field=None, max_length=100, )
    caption = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(null=True)
    #created_by = models.ForeignKey(User, related_name='posts')
    #updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        return self.class_name
