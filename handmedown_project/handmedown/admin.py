from django.contrib import admin
from .models import User, Post, Comment, Cart, Item

class UserAdmin(admin.ModelAdmin):
    model = User

admin.site.register(User, UserAdmin)
# admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Item)
admin.site.register(Cart)