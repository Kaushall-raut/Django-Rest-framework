from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def getApi(request):
   data=Student.objects.all()
   serializer=StudentSerializer(data,many=True)
   return Response(serializer.data)


@api_view(['POST'])
def postApi(request):
   serializer=StudentSerializer(data=request.data)

   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data ,status=status.HTTP_201_CREATED)
   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def putApi(request,pk):
   try:
    data=Student.objects.get(id=pk)
   except Student.DoesNotExist:
      return Response("data not found",status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'PATCH':
      serializer=StudentSerializer(data,data=request.data,partial=True)
   else:
      serializer=StudentSerializer(data,data=request.data)

   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteApi(request,pk):
   try:
      data=Student.objects.get(id=pk)
   except Student.DoesNotExist:
      return Response("data does not exist",status=status.HTTP_404_NOT_FOUND)
   
   data.delete()

   return Response("data deleted" , status=status.HTTP_204_NO_CONTENT)

   