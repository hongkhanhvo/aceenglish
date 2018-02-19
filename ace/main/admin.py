from django.contrib import admin

# Register your models here.
from .models import Course, Post, GalleryPhoto, CourseDesc

admin.site.register(Course)
admin.site.register(Post)
admin.site.register(GalleryPhoto)
admin.site.register(CourseDesc)
