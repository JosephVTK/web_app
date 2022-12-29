from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'pk',
            'author',
            'date_created',
            'is_published',
            'title',
            'content',
            'tags'
        ]