from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.

MODEL_EXAMPLE = """

from .models import MyModel

class MyModelView(DetailView):
    model = MyModel

"""