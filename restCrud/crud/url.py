from django.urls import path
from . import views

urlpatterns = [
    path("get",views.getApi, name='get'),
    path("post",views.postApi, name='post'),
    path("put/<int:pk>",views.putApi, name='put'),
    path("del /<int:pk>",views.deleteApi, name='del')
]