from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Post


# Create your views here.

class PostsList(ListView):
    template_name = "posts/index.html"
    model = Post


''' 
def posts_home(request):
    return HttpResponse("<h1>Hello</h1>")
'''


class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
