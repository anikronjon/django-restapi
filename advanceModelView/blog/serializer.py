from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'description', 'created', 'updated')