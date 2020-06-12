from fb_post.models import Comment

from .validity import is_user_valid, is_reply_content_valid

from fb_post.exceptions import InvalidCommentException

def reply_to_comment(user_id, comment_id, reply_content):
    is_user_valid(user_id)
    is_reply_content_valid(reply_content)

    try:
        comment_obj = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        raise InvalidCommentException

    parent_comment_id = comment_obj.parent_comment_id
    has_parent_comment_id = parent_comment_id

    if has_parent_comment_id:
        parent_comment_id = parent_comment_id
    else:
        parent_comment_id = comment_id
    reply_comment = Comment.objects.create(content=reply_content,
                                   commented_by_id=user_id,
                                   post_id=comment_obj.post_id,
                                   parent_comment_id=parent_comment_id)
    reply_comment_id = reply_comment.id
    return reply_comment
