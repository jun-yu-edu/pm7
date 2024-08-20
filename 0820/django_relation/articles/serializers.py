from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {"article": {"read_only": True}}

class ArticleWithCommentsSerializer(serializers.ModelSerializer):
        
    comment_set = CommentSerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'comment_set']