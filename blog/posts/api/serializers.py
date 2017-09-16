from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
)

from ..models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'draft', 'publish')


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Post


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content')


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )
    user_first_name = SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'content', 'user_first_name')

    def get_user_first_name(self, obj):
        return obj.user.first_name


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'draft', 'publish')
