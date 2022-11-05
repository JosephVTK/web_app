from django.urls import path

from .views import MyModelView

urlpatterns = [
    path('model/<pk>/', MyModelView.as_view(), name='mymodel_detail'),
]