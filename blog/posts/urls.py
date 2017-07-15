from django.conf.urls import url
from .views import PostsList, PostDetail, post_create, post_update, post_delete #CreatePost


urlpatterns = [
    url(r'^$', PostsList.as_view(), name='list'),
    url(r'^(?P<post_id>\d+)/$', PostDetail.as_view(), name='detail'),
    # url(r'^create/$', CreatePost.as_view(), name='create')
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<post_id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<post_id>\d+)/delete/$', post_delete, name='delete')
]