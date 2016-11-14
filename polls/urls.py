from django.conf.urls import url

from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index),
    #url(r'^deeper/$', views.some_else),
    ]