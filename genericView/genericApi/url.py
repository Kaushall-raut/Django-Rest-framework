from django.urls import path
from .views import StudentGeneric,StudentPutDelete

urlpatterns = [
    path("students",StudentGeneric.as_view()),
    path("students/<int:pk>",StudentPutDelete.as_view()),

]