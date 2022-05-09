from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [ 
  path('users/', views.UserList.as_view(), name='user_list'),
  path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
  path('posts/', views.PostList.as_view(), name="post_list"),
  path('posts/<int:pk>', views.PostDetail.as_view(), name="post_detail"),
  path('comments/', views.CommentList.as_view(), name="comment_list"),
  path('comments/<int:pk>', views.CommentDetail.as_view(), name="comment_detail")
]

# tunr/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.user_list, name='user_list'),
#     path('posts/', views.post_list, name='post_list'),
#     path('users/<int:pk>', views.user_detail, name='user_detail'),
#     path('posts/<int:pk>', views.post_detail, name='post_detail'),
#     path('users/new', views.user_create, name='user_create'),
#     path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
#     path('users/<int:pk>/delete', views.user_delete, name='user_delete'),
# ]