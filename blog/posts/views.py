from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
from .models import Post


from .forms import CreatePostForm
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
    pk_url_kwarg = "post_id"


class CreatePost(FormView):
    form_class = CreatePostForm
    template_name = "posts/create_post.html"
    success_url = "/posts/create/"

    def form_valid(self, form):
        form.save()
        return super(CreatePost, self).form_valid(form)
