from django.shortcuts import render
from django.views.generic import DetailView, ListView

from rest_framework import viewsets

from .models import Article, Tag
from .serializers import ArticleSerializer

# Create your views here.
class ArticleDetailView(DetailView):
    model = Article

class ArticleListView(ListView):
    queryset = Article.objects.all().select_related('author').prefetch_related('tags')

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class TagDetailView(DetailView):
    queryset = Tag.objects.all().prefetch_related('articles__tags', 'articles__author')