from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'photo_url', 'password',)

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = ('title', 'album', 'preview_url', 'artist',)