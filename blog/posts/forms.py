from django import forms

from .models import Post


# class CreatePostForm(forms.ModelForm):
#
#     # def save(self):
#     #     form = super(CreatePostForm, self).save(self, self.kwargs)
#     #     form.save()
#
#
#     class Meta:
#         model = Post
#         fields = [
#             "title",
#             "content"
#         ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content"
        ]
