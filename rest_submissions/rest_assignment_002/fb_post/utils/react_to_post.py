from fb_post.models import Reaction

from .validity import is_user_valid, is_post_valid, is_reaction_type_valid

from .common_utils import update_or_undo_reaction_obj


def react_to_post(user_id, post_id, reaction_type):
    is_user_valid(user_id)
    is_post_valid(post_id)
    is_reaction_type_valid(reaction_type)

    user_reaction_to_post_reaction_obj = Reaction.objects\
    .filter(reacted_by_id=user_id, post_id=post_id).first()
 
    is_user_reacted_to_post = user_reaction_to_post_reaction_obj

    if is_user_reacted_to_post:
        update_or_undo_reaction_obj(user_reaction_to_post_reaction_obj, reaction_type)
    else:
        Reaction.objects.create(post_id=post_id, reaction=reaction_type,
                                reacted_by_id=user_id)