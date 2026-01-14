from rest_framework import serializers

from posts.models import Comment, Group, Post


class AuthorMixin(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = (fields,)


class PostSerializer(AuthorMixin):

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(AuthorMixin):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
