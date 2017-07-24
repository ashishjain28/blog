from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from models import Post
from forms import PostForm

# from .forms import CreatePostForm
# Create your views here.


class PostsList(ListView):
    template_name = "posts/index.html"
    model = Post
    #ordering = "-updated"
    paginate_by = 2


''' 
def posts_home(request):
    return HttpResponse("<h1>Hello</h1>")
'''


class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    #pk_url_kwarg = "slug"


# class CreatePost(FormView):
#     form_class = CreatePostForm
#     template_name = "posts/create_post.html"
#     success_url = "/posts/create/"
#
#     def form_valid(self, form):
#         form.save()
#         return super(CreatePost, self).form_valid(form)

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    # if request.method == "POST":
    #     print request.POST
    context = {
        "form": form
    }
    return render(request, "posts/create_post.html", context)


def post_update(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "posts/create_post.html", context)


def post_delete(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    instance.delete()
    return redirect('posts:list')
