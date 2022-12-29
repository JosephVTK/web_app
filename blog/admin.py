from django.contrib import admin

from .models import Article, Tag

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    prepopulated_fields = prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    model = Tag


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
