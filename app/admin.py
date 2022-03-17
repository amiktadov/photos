from django.contrib import admin

from app.models import Post, Image, Reaction, Size, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Reaction)
admin.site.register(Size)
admin.site.register(Comment)
