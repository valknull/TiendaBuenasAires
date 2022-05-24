from django.shortcuts import render
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductoSerializer
from core.models import Producto, myUser
# Create your views here.

class producto_create(APIView):
    def post(self, request , format = None):
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
