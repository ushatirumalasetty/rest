from django.shortcuts import render

from .exceptions import *

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CreatePostRequest:
    def __init__(self, user_id, content=''):
        self.user_id = user_id
        self.content = content

class CreatePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField()

    def create(self, validated_data):
        return CreatePostRequest(**validated_data)
        


class CreatePostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()


@api_view(["POST"])
def create_new_post(request):
    serializer = CreatePostRequestSerializer(data = request.data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        request_obj = serializer.save()
        from .utils import create_post
        try:
            new_post_obj = create_post(request_obj.user_id, request_obj.content)
            
        except InvalidUserException:
            return Response(status=404)
        except InvalidPostContent:
            return Response(status=404)
        response_serializer = CreatePostResponseSerializer(new_post_obj)
        return Response(response_serializer.data, status=201)
    else:
        Response(serializer.errors)

class User:
    def __init__(self, user_id, name, profile_pic):
        self.name = name
        self.user_id = user_id
        self.profile_pic = profile_pic

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name = serializers.CharField()
    profile_pic = serializers.URLField(allow_null=True, required=False)

class Reactions:
    def __init__(self, count, type):
        self.count = count
        self.type = type

class ReactionsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    type = serializers.ListField()


class Replies:
    def __init__(self, comment_id, commenter, commented_at, comment_content, reactions):
        self.comment_id = comment_id
        self.commenter = commenter
        self.commented_at = commented_at
        self.comment_content = comment_content
        self.reactions = reactions

class RepliesSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = UserSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField()
    reactions = ReactionsSerializer()



class CommentsSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = UserSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField()
    reactions = ReactionsSerializer()
    replies_count = serializers.IntegerField()
    replies = RepliesSerializer()

class Post:
    def __init__(self, post_id, posted_by, posted_at, post_content, reactions, comments, comments_count):
        self.post_id = post_id
        self.posted_by = posted_by
        self.posted_at = posted_at
        self.post_content = post_content
        self.reactions = reactions
        self.comments = comments
        self.comments_count = comments_count

class PostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    posted_by = UserSerializer()
    posted_at = serializers.DateTimeField()
    post_content = serializers.CharField()
    reactions = ReactionsSerializer()
    comments = CommentsSerializer(many=True)
    comments_count = serializers.IntegerField()

@api_view(["GET"])
def get_new_post(request,post_id):
    from .utils import get_post
    try:
        data = get_post(post_id)
    except:
        return Response(status=404)
    serializer = PostSerializer(data = data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors)


class CreateReplyToCommentRequest:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content

class CreateReplyToCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField()

    def create(self, validated_data):
        return CreateReplyToCommentRequest(**validated_data)


class CreateReplyToCommentResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()

@api_view(["POST"])
def new_reply_to_comment(request, comment_id):
    serializer = CreateReplyToCommentRequestSerializer(data = request.data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        request_obj = serializer.save()
        from .utils import reply_to_comment
        try:
            new_reply_to_comment_obj = reply_to_comment(request_obj.user_id,  comment_id, request_obj.content)
        except InvalidUserException:
            return Response(status=404)
        except InvalidReplyContent:
            return Response(status=404)
        response_serializer = CreateReplyToCommentResponseSerializer(new_reply_to_comment_obj)
        return Response(response_serializer.data, status=201)
    else:
        Response(serializer.errors)








class CreateReactToPostRequest:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type



class CreateReactToPostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.CharField()

    def create(self, validated_data):
        return CreateReactToPostRequest(**validated_data)


@api_view(["POST"])
def new_react_to_post(request, post_id):
    serializer = CreateReactToPostRequestSerializer(data = request.data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        request_obj = serializer.save()
        from .utils import react_to_post
        try:
            react_to_post(request_obj.user_id, post_id, request_obj.reaction_type)
        except InvalidUserException:
            return Response(status=404)
        except InvalidPostException:
            return Response(status=404)
        except InvalidReactionTypeException:
            return Response(status=400)
        return Response(status=201)
    else:
        Response(serializer.errors)





class CreateReactToCommentRequest:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type



class CreateReactToCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type = serializers.CharField()

    def create(self, validated_data):
        return CreateReactToCommentRequest(**validated_data)


@api_view(["POST"])
def new_react_to_comment(request, comment_id):
    serializer = CreateReactToCommentRequestSerializer(data = request.data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        request_obj = serializer.save()
        from fb_post.utils import react_to_comment
        try:
            react_to_comment(request_obj.user_id, comment_id, request_obj.reaction_type)
        except InvalidUserException:
            return Response(status=404)
        except InvalidCommentException:
            return Response(status=404)
        return Response(status=201)
    else:
        Response(serializer.errors)







class DeletePostRequest:
    def __init__(self, user_id):
        self.user_id = user_id

class DeletePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return DeletePostRequest(**validated_data)

@api_view(["POST"])
def new_delete_post(request, post_id):
    serializer = DeletePostRequestSerializer(data = request.data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        request_obj = serializer.save()
        from .utils import delete_post
        try:
            delete_post(request_obj.user_id, post_id)
        except InvalidUserException:
            return Response(status=404)
        except InvalidPostException:
            return Response(status=404)
        return Response(status=201)
    else:
        Response(serializer.errors)





class CreateCommentRequest:
    def __init__(self, user_id, content=''):
        self.user_id = user_id
        self.content = content


class CreateCommentRequestSerialize(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField()

    def create(self, validated_data):
        return CreateCommentRequest(**validated_data)

class CreateCommentResponseSerialize(serializers.Serializer):
    id = serializers.IntegerField()

@api_view(["POST"])
def new_create_comment(request, post_id):
    serializer = CreateCommentRequestSerialize(data = request.data)
    is_serializer_valid = serializer.is_valid()
    if is_serializer_valid:
        request_obj = serializer.save()
        from .utils import create_comment
        try:
            new_comment_obj = create_comment(request_obj.user_id, post_id, request_obj.content)
        except InvalidUserException:
            return Response(status=404)
        except InvalidPostException:
            return Response(status=404)
        except InvalidCommentException:
            return Response(status=404)
        response_serializer = CreateCommentResponseSerialize(new_comment_obj)
        return Response(response_serializer.data, status=201)
    else:
        Response(serializer.errors)



