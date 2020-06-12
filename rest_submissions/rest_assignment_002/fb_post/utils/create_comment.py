from fb_post.models import Comment

from .validity import is_user_valid, is_post_valid, is_comment_content_valid

def create_comment(user_id, post_id, comment_content):
    is_comment_content_valid(comment_content)
    is_user_valid(user_id)
    is_post_valid(post_id)

    new_comment_obj = Comment.objects.create(content=comment_content,
                                             commented_by_id=user_id,
                                             post_id=post_id)
    new_comment_obj_id = new_comment_obj.id
    return new_comment_obj
