from django.shortcuts import render

# Create your views here.

from rest_framework import generics,mixins
from .models import Student
from .serializers import StudentSerializer


class StudentGeneric(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin):
    
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class StudentPutDelete(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
     queryset=Student.objects.all()
     serializer_class=StudentSerializer

     def get(self,request,*args,**kwargs): #to retrive single data 
        return self.retrieve(request,*args,**kwargs)
     
     def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
     
     def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

