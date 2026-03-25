from rest_framework import serializers
from .models import (
    UserProfile, Post, Comment, CommentLike, SavePost, SavePostItem, Story, Hashtag
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username',]


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id']


class PostSerializer(serializers.ModelSerializer):
    hashtag = HashtagSerializer(many=True, read_only=True)
    people = UserProfileSerializer(many=True, read_only=True)
    created_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'music', 'description', 'hashtag', 'people', 'created_date']


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'text', 'created_date']


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['id', 'comment', 'user', 'like']


class SavePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavePost
        fields = ['id', 'user']


class SavePostItemSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = SavePostItem
        fields = ['id', 'save_post', 'post']


class StorySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Story
        fields = ['id', 'user', 'file', 'created_date']