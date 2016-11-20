from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog_list, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^log/$', views.log, name='log'),
    url(r'^(?P<id>[0-9]+)/$', views.blog_detail, name='detail'),
    url(r'^create/$', views.blog_create, name='create'),
    url(r'^(?P<id>[0-9]+)/update/$', views.blog_update, name='update'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.blog_delete, name='delete'),
]