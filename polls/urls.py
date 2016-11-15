from django.conf.urls import url

from . import views
from django.conf.urls import include

app_name = 'polls'
    # 3 Add the 3 views
    # The data surrounded by parentheses is sent to the function
    # ?P<question_id> defines the name for the data within
    # the parentheses
    # [0-9]+ says we will match 1 or more numbers
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^index/$', views.index),
    url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/result/$', views.result, name='result')
    #url(r'^deeper/$', views.some_else),
    ]
#minutul 7:27