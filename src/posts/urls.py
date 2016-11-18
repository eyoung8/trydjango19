from django.conf.urls import url
from django.contrib import admin

from .views import post_list, post_create, post_detail, post_update, post_delete

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[-\w]+)/$', post_detail, name='detail'),
    url(r'^(?P<id>[-\w]+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>[-\w]+)/delete/$', post_delete, name='delete'),
]
