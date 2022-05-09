from rest_framework import serializers
from .models import User, Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    user_url = serializers.ModelSerializer.serializer_url_field(
    view_name='user_detail'
    )
   
    
    class Meta:
        model = User
        fields = ('id', 'user_url','username', 'first_name', 'last_name', 'photo_url', 'password', 'posts', 'comments' )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )    
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    post_url = serializers.ModelSerializer.serializer_url_field(
    view_name='post_detail'
    )
    class Meta:
        model = Post
        fields = ('id', 'user', 'user_id', 'post_url', 'name', 'item_url', 'price', 'description', 'comments')



class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )    
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        source='post'
    )   

    # comment_url = serializers.ModelSerializer.serializer_url_field(
    # view_name='comment_detail'
    # )

    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'user_id', 'user', 'post', 'description', 'date')

