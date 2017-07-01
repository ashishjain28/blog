from django.contrib import admin

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_display_links = ['updated', 'created']
    list_filter = ['created', 'updated']
    search_fields = ['content']

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

