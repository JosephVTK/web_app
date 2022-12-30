from django.contrib import admin

from .models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    model = Document

admin.site.register(Document, DocumentAdmin)