from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^uploadFiles/$', views.upload_files, name='upload_files'),
    url(r'^fileList/$', views.uploaded_file_list, name='uploaded_file_list'),
    url(r'^fileList/(?P<pk>\d+)/$', views.file_detail, name='file_detail'),
    url(r'^fileList/(?P<pk>\d+)/edit/$', views.upload_edit, name='upload_edit'),
]
