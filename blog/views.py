from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer, CategorySerializer, AuthorSerializer
from .models import Category, Blog, Author
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt 

# Create your views here.
# create category view
# @api_view(['POST'])
# @csrf_exempt
# def create_category(request):
#     serializer = CategorySerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class categoryView(APIView):
    def post(request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# getting all category in db
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

# updating category details
@api_view(['PUT'])
@csrf_exempt
def update_category_details(request, pk):
    # pk = kwargs.get('pk')
    try:
        category = Category.objects.filter(id = pk).first()
        print("category", category)
    except Category.DoesNotExist:
        return Response({"message":"Category does not exist"}, status=status.HTTP_404_NOT_FOUND)
    print("request", request.data)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# delete category
@api_view(['DELETE'])
def delete_category(request, pk):
    #   pk = kwargs.get('pk')
      try:
          category = Category.objects.filter(id = pk).first()

      except Category.DoesNotExist:
          return Response({"message":"Category does not exist"}, status=status.HTTP_404_NOT_FOUND)
      
      category.delete()

      return Response({"message":"Category deleted"}, status=status.HTTP_204_NO_CONTENT)


# *************Blog***************
# create blog
@api_view(['POST'])
@csrf_exempt
def create_blog_details(request):
    serializer = BlogSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get all blogs
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# get single blog details
@api_view(['GET'])
@permission_classes([AllowAny])
def get_single_blog_details(request, pk):
    # pk = kwargs.get('pk')
    try:
        blog = Blog.objects.filter(id = pk).first()
    
    except Blog.DoesNotExist:
        return Response({"message":"Blog does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BlogSerializer(blog)
    return Response(serializer.data, status=status.HTTP_200_OK)



# updating blogs details
@api_view(['PUT'])
@csrf_exempt
def update_blog_details(request, pk):
    # pk = kwargs.get('pk')
    try:
        blog = Blog.objects.filter(id = pk).first()
    
    except Blog.DoesNotExist:
        return Response({"message":"Blog does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BlogSerializer(instance=blog, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# delete blog
@api_view(['DELETE'])
def delete_blog_details(request, pk):
    # pk = kwargs.get('pk')
    try:
        blog = Blog.objects.filter(id = pk).first()
    
    except Blog.DoesNotExist:
        return Response({"message":"Blog does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    blog.delete()
    return Response({"message":"Blog deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Author endpoints
@api_view(['POST'])
@csrf_exempt
def add_author_details(request):
    serializer = AuthorSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_authors(request):
    author = Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# get single author details
@api_view(['GET'])
@permission_classes([AllowAny])
def get_single_author_details(request, pk):
    try:
        author = Author.objects.filter(id = pk).first()
    
    except Author.DoesNotExist:
        return Response({"message":"Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)

# delete blog
@api_view(['DELETE'])
def delete_author_details(request, pk):
    try:
        author = Author.objects.filter(id = pk).first()
    
    except Author.DoesNotExist:
        return Response({"message":"Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    author.delete()
    return Response({"message":"Author deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# updating blogs details
@api_view(['PUT'])
@csrf_exempt
def update_author_details(request, pk):
    # pk = kwargs.get('pk')
    try:
        author = Author.objects.filter(id = pk).first()
    
    except Author.DoesNotExist:
        return Response({"message":"Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuthorSerializer(instance=author, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
