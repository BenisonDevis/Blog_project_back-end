from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from .models import *
from .serializers import *



# def demo(self, request):
#     return HttpResponse('helo ')


class BlogCreateApiView(APIView):
    def get(self, request):
        blog_list = Blog.objects.all()
        serializer = BlogCreateSerializer(blog_list, many=True)
        return Response(
            {
                'success': True,
                'data': serializer.data,
                'message': 'Blog listed successfuly done',
                'error': None
            },
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        serializer = BlogCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': True,
                    'data': serializer.data,
                    'message': 'Blog created Successfully done',
                    'error': None
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'success': False,
                'data': serializer.errors,
                'message': 'Blog Created falied',
                'error': 'Error'
            }
        )
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

