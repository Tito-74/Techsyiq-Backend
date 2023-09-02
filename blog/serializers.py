from rest_framework import serializers
from .models import Category, Blog, Author
# category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# blog serializer
class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image', 'date_published', 'author' ,'category_name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'firstName', 'lastName', 'image', 'title']