from rest_framework import generics
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .models import User, Post, Comment

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer





# from django.shortcuts import render, redirect
# from .models import User, Post
# from .forms import UserForm
# # Create your views here.


# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'handmedown/user_list.html', {'users': users})

# def user_detail(request, pk):
#     user = User.objects.get(id=pk)
#     return render(request, 'handmedown/user_detail.html', {'user': user})   

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'handmedown/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     return render(request, 'handmedown/post_detail.html', {'post': post})

### CREATE ### CREATE ### CREATE ### CREATE ### CREATE ### CREATE ### CREATE ###

# def user_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', pk=user.pk)
#     else:
#         form = UserForm()
#     return render(request, 'handmedown/user_form.html', {'form': form})

### EDIT ### EDIT ### EDIT ### EDIT ### EDIT ### EDIT ### EDIT ### EDIT ### EDIT ###

# def user_edit(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', pk=user.pk)
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'handmedown/user_form.html', {'form': form})

### DELETE ### DELETE ### DELETE ### DELETE ### DELETE ### DELETE ### DELETE ###

# def user_delete(request, pk):
#     User.objects.get(id=pk).delete()
#     return redirect('artist_list')



