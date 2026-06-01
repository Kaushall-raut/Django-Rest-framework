from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here.



class StudentApi(APIView):

    def get(self,request,pk=None):
        if pk:
            data=Student.objects.get(id=pk)
            serializer=StudentSerializer(data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            data=Student.objects.all()
            serializer=StudentSerializer(data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        data=Student.objects.get(id=pk)

        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        data=Student.objects.get(id=pk)

        data.delete()
        return Response("Data deleted successfully",status=status.HTTP_204_NO_CONTENT)