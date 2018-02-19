"""ace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^base$', views.base, name='base'),
    url(r'^about$', views.about, name='about'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^achievement$', views.achievement, name='achievement'),
    url(r'^post/(?P<pk>\d+)$', views.post, name='post'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^courses$', views.courses, name='courses'),
    url(r'^toeic$', views.toeic, name='toeic'),
    url(r'^vstep$', views.vstep, name='vstep'),
    url(r'^giao-tiep$', views.giaotiep, name='giaotiep'),
    url(r'^ielts$', views.ielts, name='ielts'),

    url(r'^img/hinh-anh-lop-hoc/(?P<pk>\d+)$', views.img, name='img'),

    url(r'^admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #at the end
