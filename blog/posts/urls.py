from django.conf.urls import url
from .views import PostsList, PostDetail, post_create, post_update, post_delete #CreatePost


urlpatterns = [
    url(r'^$', PostsList.as_view(), name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[a-zA-Z0-9-]*)/$', PostDetail.as_view(), name='detail'),
    # url(r'^create/$', CreatePost.as_view(), name='create')
    url(r'^(?P<slug>[a-zA-Z0-9-]*)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[a-zA-Z0-9-]*)/delete/$', post_delete, name='delete')
]