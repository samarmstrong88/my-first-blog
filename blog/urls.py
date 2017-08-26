from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name ='post_list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail_list, name ='detail_list')
]
