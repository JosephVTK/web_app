from django.urls import path
from .views import ArticleDetailView, ArticleListView, ArticleViewSet, TagDetailView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/view/<slug>/', ArticleDetailView.as_view(), name='article_detail'),

    path('tags/<pk>/', TagDetailView.as_view(), name='tag_detail'),
]
