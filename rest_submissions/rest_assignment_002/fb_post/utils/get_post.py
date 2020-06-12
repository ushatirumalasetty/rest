from fb_post.models import Post

from .validity import is_post_valid

from .dict_post_details import get_dict_details_of_post

#task - 13
def get_post(post_id):
    is_post_valid(post_id)

    post_obj = Post.objects\
       .select_related('posted_by')\
       .prefetch_related('comments', 'reaction', 'comments__reaction',
                         'comments__commented_by')\
       .filter(id=post_id)\
       .first()

    return get_dict_details_of_post(post_obj)
