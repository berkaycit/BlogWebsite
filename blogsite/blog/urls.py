from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), 
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/(?P<pk>\w+)/$', views.post_cat, name='post_cat'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<article_id>[0-9]+)/like/$', views.post_like, name='post_like'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/(?P<profile_id>\d+)/$', views.user_profile, name='user_profile'),
    url(r'^profile/(?P<profile_id>\d+)/edit/$', views.profile_edit, name='profile_edit'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)