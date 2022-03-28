from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class Size(models.Model):
    title = models.CharField(max_length=50)
    width = models.IntegerField()
    height = models.IntegerField()


class Post(BaseModel):
    description = models.CharField(max_length=250, blank=True, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    coords = models.CharField(max_length=255, blank=True, null=True)


class Reaction(BaseModel):
    CHOICE = (
        ('smile', '😊'),
        ('sad', '☹'),
        ('lol', '😂'),
        ('angry', '😡'),
        ('hard', '♥')
    )
    date_del = models.DateTimeField(default=None, null=True)
    emoji = models.CharField(max_length=50, choices=CHOICE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')


class Comment(BaseModel):
    date_del = models.DateTimeField(default=None, null=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
