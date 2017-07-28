from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post
from .forms import PostForm

# from .forms import CreatePostForm
# Create your views here.


class PostsList(ListView):
    template_name = "posts/index.html"
    model = Post
    #ordering = "-updated"
    paginate_by = 2

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset_list = Post.objects.all()
            query = self.request.GET.get('q')
            if query:
                return queryset_list.filter(
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                ).distinct()
            return queryset_list
        else:
            return Post.objects.active()


''' 
def posts_home(request):
    return HttpResponse("<h1>Hello</h1>")
'''


class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    #pk_url_kwarg = "slug"

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Post.objects.all().filter(slug=self.kwargs['slug'])

        else:
            raise Http404


# class CreatePost(FormView):
#     form_class = CreatePostForm
#     template_name = "posts/create_post.html"
#     success_url = "/posts/create/"
#
#     def form_valid(self, form):
#         form.save()
#         return super(CreatePost, self).form_valid(form)

def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    # if request.method == "POST":
    #     print request.POST
    context = {
        "form": form
    }
    return render(request, "posts/create_post.html", context)


def post_update(request, slug=None):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "posts/create_post.html", context)


def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    return redirect('posts:list')
