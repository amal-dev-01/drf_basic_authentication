from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from basic.models import Student
from basic.serializers import StudentSerializer
from rest_framework import viewsets  
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    
