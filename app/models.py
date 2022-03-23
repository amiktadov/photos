from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.forms import DateTimeField


class Size(models.Model):
    title = models.CharField(max_length=50)
    width = models.IntegerField()
    height = models.IntegerField()


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    coords = models.CharField(max_length=255, blank=True, null=True)


class Reaction(models.Model):
    CHOICE = (
        ('smile', '😊'),
        ('sad', '☹'),
        ('lol', '😂'),
        ('angry', '😡'),
        ('hard', '♥')
    )
    date_add = models.DateTimeField(auto_now_add=True)
    date_del = models.DateTimeField(default=None, null=True)
    emoji = models.CharField(max_length=50, choices=CHOICE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')


class Comment(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_del = models.DateTimeField(default=None, null=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
