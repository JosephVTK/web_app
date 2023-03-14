from django.urls import path
from .views import FaceTemplateView

urlpatterns = [
    path('', FaceTemplateView.as_view(), name='face'),
]
