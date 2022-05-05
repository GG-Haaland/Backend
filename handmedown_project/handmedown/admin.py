from django.contrib import admin
from .models import User, Post, Comment, Cart, Item

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Item)
admin.site.register(Cart)