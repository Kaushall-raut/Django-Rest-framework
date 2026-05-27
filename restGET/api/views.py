from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .searializer import StudentSerializer

# Create your views here.
@api_view(['GET'])
def home(request):
    data=Students.objects.all()
    serializer=StudentSerializer(data,many=True)
    return Response(serializer.data)