from django.shortcuts import render
from .models import Post, Category
from .serializer import CategorySerializer, PostSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# GET AND POST
class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('id','name')
    search_fields = ('id', 'name')


# UPDATE AND PU
class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# DELETE
class CategoryDestroyView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.order_by('-pk')
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','name')
    # filter_fields = ('id','name')
    search_fields = ('id', 'name')


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-pk')
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('id','name')
    search_fields = ['name']

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
