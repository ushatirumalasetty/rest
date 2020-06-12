from fb_post.models import Reaction

from.validity import is_user_valid

def get_posts_reacted_by_user(user_id):
    is_user_valid(user_id)

    post_ids = Reaction.objects.filter(reacted_by=user_id)\
        .values_list("post_id", flat=True)
    list_of_post_ids = list(post_ids)

    return list_of_post_ids
