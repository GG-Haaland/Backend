from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo_url = models.TextField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=100)
    # item = models.CharField(max_length=100)
    # item_url = models.TextField()
    # price = models.CharField(max_length=10)
    # description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    description = models.CharField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.description


class Item(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    item_url = models.TextField()
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='carts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')

    def __str__(self):
        return self.user