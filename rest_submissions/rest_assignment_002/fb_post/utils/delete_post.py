from fb_post.models import Post

from .validity import is_user_valid, is_post_valid

from fb_post.exceptions import UserCannotDeletePostException

def delete_post(user_id, post_id):
    is_user_valid(user_id)
    post_obj = is_post_valid(post_id)

    is_user_creater_of_the_post = (post_obj.posted_by_id == user_id)

    if is_user_creater_of_the_post:
        post_obj.delete()
    else:
        raise UserCannotDeletePostException
