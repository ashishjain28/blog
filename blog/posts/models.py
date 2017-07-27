from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now_add=False, auto_now=False)

    verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        # return '/posts/%s' %(self.id)
        return reverse('posts:detail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-updated"]


def pre_save_post(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug += '-1'
        exists = Post.objects.filter(slug=slug).exists()
        while exists:
            value = int(slug.split('-')[-1]) + 1
            slug = '-'.join(slug.split('-')[:-1]) + '-' + str(value)
            exists = Post.objects.filter(slug=slug).exists()
    instance.slug = slug

pre_save.connect(pre_save_post, sender=Post)
