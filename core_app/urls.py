from django.urls import path

MODEL_EXAMPLE = """
from .views import MyModelView

urlpatterns = [
    path('model/<pk>/', MyModelView.as_view(), name='mymodel_detail'),
]

"""