from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        # return '/posts/%s' %(self.id)
        return reverse('posts:detail', kwargs={"post_id": self.id})
