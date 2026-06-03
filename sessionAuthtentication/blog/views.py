from django.shortcuts import render

# Create your views here.

from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def blog_list(request):
    if request.method == 'GET':
        data=Student.objects.all()
        serializer=StudentSerializer(data,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)