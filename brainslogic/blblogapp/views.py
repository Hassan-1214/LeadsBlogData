from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from blblogapp.models import Blog
from blblogapp.serializers import BlogSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.

class BlogApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Blog.objects.all().filter(blog_isactive=True)
    serializer_class = BlogSerializer
    # permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



   
    # def get(self, request, *args, **kwargs):
    #     queryset = BlogModel.objects.all().filter(blog_isactive=True)
    #     serializer = BlogSerializer(queryset, many = True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request, *args, **kwarfs):
    #     serializer = BlogSerializer(data=request.data)
       
    #     if serializer.is_valid():
    #         print(request.data)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


