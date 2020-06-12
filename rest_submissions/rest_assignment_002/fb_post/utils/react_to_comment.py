from fb_post.models import Reaction

from .validity import is_user_valid, is_comment_valid, is_reaction_type_valid

from .common_utils import update_or_undo_reaction_obj

def react_to_comment(user_id, comment_id, reaction_type):
    is_user_valid(user_id)
    is_comment_valid(comment_id)
    is_reaction_type_valid(reaction_type)

    user_reaction_to_comment_reaction_obj = Reaction.objects\
    .filter(reacted_by_id=user_id, comment_id=comment_id).first()
    is_user_reacted_to_comment = user_reaction_to_comment_reaction_obj

    if is_user_reacted_to_comment:
        update_or_undo_reaction_obj(user_reaction_to_comment_reaction_obj, reaction_type)
    else:
        Reaction.objects.create(comment_id=comment_id, reaction=reaction_type,
                                reacted_by_id=user_id)
