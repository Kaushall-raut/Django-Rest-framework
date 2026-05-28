from django.urls import path
from . import views

urlpatterns = [
    path("get",views.getApi, name='get')
]