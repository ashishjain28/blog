from django.conf.urls import url
from .views import PostsList, PostDetail, CreatePost


urlpatterns = [
    url(r'^$', PostsList.as_view()),
    url(r'^(?P<post_id>\d+)/$', PostDetail.as_view(), name='detail'),
    url(r'^create/$', CreatePost.as_view(), name='create')
]