from django.conf.urls import url
from .views import PostsList, PostDetail


urlpatterns = [
    url(r'^$', PostsList.as_view()),
    url(r'^(?P<pk>[1-9]*)/$', PostDetail.as_view())
]