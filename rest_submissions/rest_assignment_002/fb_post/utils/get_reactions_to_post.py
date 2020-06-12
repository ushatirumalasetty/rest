from fb_post.models import Reaction

from .validity import is_post_valid

def get_reactions_to_post(post_id):
    is_post_valid(post_id)
    reaction_objs = Reaction.objects.filter(post_id=post_id)\
    .select_related("reacted_by")
    return [
        {
            "user_id":reaction_obj.reacted_by_id,
            "name":reaction_obj.reacted_by.name,
            "profile_pic":reaction_obj.reacted_by.profile_pic,
            "reaction":reaction_obj.reaction
        }
        for reaction_obj in reaction_objs
    ]
