from django.conf.urls import url
from . import views 

app_name = 'blog'

#/post/
urlpatterns = [ 
    url(r'^$', views.index, name ='index'),
#post/ID/
    url(r'^details/(?P<id>\d+)/$', views.details, name ='details'),

  
]