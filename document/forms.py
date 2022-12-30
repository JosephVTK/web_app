from django import forms
from .models import Document
from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _

class DocumentUploadForm(forms.Form):
    file_field = forms.FileField(required=True)
    title = forms.CharField(max_length=64, required=False)
    summary = forms.CharField(max_length=1024*10, required=False, widget=forms.Textarea)

    def clean_file_field(self):
        MAX_DOCUMENT_SIZE = 1024 * 1024 * 10 # 10 Megabytes
        file_field = self.cleaned_data['file_field']
        print (dir(file_field))
        if file_field.size > MAX_DOCUMENT_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(MAX_DOCUMENT_SIZE), filesizeformat(file_field.size)))
        return file_field