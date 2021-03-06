from rest_framework import serializers
from .models import MainUser, Category, News, Like, Comment
from django.contrib.auth.models import User


class MainUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class MainUserSerializer2(serializers.ModelSerializer):
     class Meta:
         model = MainUser
         fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


