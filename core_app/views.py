from django.shortcuts import render
from django.views.generic import DetailView

from .models import MyModel

# Create your views here.
class MyModelView(DetailView):
    model = MyModel