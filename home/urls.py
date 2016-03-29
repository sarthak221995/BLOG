from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^me/$', views.me, name='me'),
    url(r'^mee/$', views.mee, name='mee'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<tag_field>[A-Z]+)/$', views.post_tagdetail, name='post_tagdetail'),
    url(r'^$', views.post_list, name='post_list'),
    
]