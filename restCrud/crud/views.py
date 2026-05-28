from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializer import StudentSerializer
# Create your views here.

@api_view(['GET'])
def getApi(request):
   data=Student.objects.all()
   serializer=StudentSerializer(data,many=True)
   return Response(serializer.data)