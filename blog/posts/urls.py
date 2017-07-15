from django.conf.urls import url
from .views import PostsList, PostDetail, post_create, post_update #CreatePost


urlpatterns = [
    url(r'^$', PostsList.as_view()),
    url(r'^(?P<post_id>\d+)/$', PostDetail.as_view(), name='detail'),
    # url(r'^create/$', CreatePost.as_view(), name='create')
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<post_id>\d+)/update/$', post_update, name='update')
]