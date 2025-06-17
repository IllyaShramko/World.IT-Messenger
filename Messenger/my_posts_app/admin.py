from django.contrib import admin
from .models import Post, Image, Album, Tag, Link
# Register your models here.

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Album)
admin.site.register(Tag)
admin.site.register(Link)