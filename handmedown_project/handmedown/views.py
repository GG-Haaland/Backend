from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Post, Comment  # ...your other models
from .serializers import UserSerializer, PostSerializer, CommentSerializer # ...your other serializers

# from .models import User, Post, Comment

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(users)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailByUsername(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)

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

# @api_view(['GET', 'POST', 'DELETE'])
# def user_list(request):
#     if request.method == 'GET':
#         users = Post.objects.all()
        
#         username = request.query_params.get('username', None)
#         if username is not None:
#             users = users.filter(username__icontains=username)
        
#         users_serializer = UserSerializer(users, many=True)
#         return JsonResponse(users_serializer.data, safe=False)
#         # 'safe=False' for objects serialization
 
#     elif request.method == 'POST':
#         user_data = JSONParser().parse(request)
#         user_serializer = UserSerializer(data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         count = User.objects.all().delete()
#         return JsonResponse({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# ##################################
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):
#     try: 
#         user = User.objects.get(pk=pk) 
#     except User.DoesNotExist: 
#         return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         user_serializer = UserSerializer(user) 
#         return JsonResponse(user_serializer.data) 
 
#     elif request.method == 'PUT': 
#         user_data = JSONParser().parse(request) 
#         user_serializer = UserSerializer(tutorial, data=user_data) 
#         if user_serializer.is_valid(): 
#             user_serializer.save() 
#             return JsonResponse(user_serializer.data) 
#         return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         user.delete() 
#         return JsonResponse({'message': 'user was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


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



