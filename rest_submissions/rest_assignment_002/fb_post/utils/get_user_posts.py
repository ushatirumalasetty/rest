from fb_post.models import Post

from .validity import is_user_valid

from .dict_post_details import get_dict_details_of_post


def get_user_posts(user_id):
    is_user_valid(user_id)

    post_objs = list(
        Post.objects\
        .select_related('posted_by')\
        .prefetch_related('comments', 'reaction', 
                          'comments__reaction', 'comments__commented_by')\
        .filter(posted_by_id=user_id)
    )

    return  [get_dict_details_of_post(post_obj) for post_obj in post_objs]
