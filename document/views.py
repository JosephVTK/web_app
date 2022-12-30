from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import DocumentUploadForm
from .models import Document

# Create your views here.
class DocumentUploadView(LoginRequiredMixin, FormView):
    form_class = DocumentUploadForm
    template_name = "document/document_upload.html"
    success_url = reverse_lazy('document_upload')

    def form_invalid(self, form):
        print ("Invalid")
        return super().form_invalid(form)

    def form_valid(self, form):
        file = form.cleaned_data['file_field']
        user = self.request.user

        if user.documents.all().count() < 10:
            Document.objects.create(user=user, file=file, title=form.cleaned_data.get('title', ''), summary=form.cleaned_data.get('summary', ''))
        
        return super().form_valid(form)