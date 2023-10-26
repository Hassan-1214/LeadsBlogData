from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from blblogapp.models import Blog, Comment
from blblogapp.serializers import BlogSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.

class BlogApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentApiView(APIView):
    queryset = Blog.objects.all()
    serializer_class = CommentSerializer

   
class CommentApi(APIView):
  
    def get(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

