
from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    user_image = models.ImageField(upload_to='user_photo/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user_network = models.URLField(null=True, blank=True)
    date_register = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='following_set', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='followers_set', on_delete=models.CASCADE)


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=100)


class Post(models.Model):
    music = models.FileField(upload_to='post_music/', null=True, blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    description = models.TextField(null=True, blank=True)
    people_tagged = models.ManyToManyField(UserProfile, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='post_content/')


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


class SavePost(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class SavePostItem(models.Model):
    save_post = models.ForeignKey(SavePost, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='stories/')
    created_date = models.DateTimeField(auto_now_add=True)



class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)