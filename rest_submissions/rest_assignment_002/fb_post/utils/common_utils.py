def update_or_undo_reaction_obj(reaction_obj, reaction_type):
    is_undo_reaction = reaction_obj.reaction == reaction_type
    if is_undo_reaction:
        undo_reaction(reaction_obj)
    else:
        update_reaction(reaction_obj, reaction_type)
    
def undo_reaction(reaction_obj):
    reaction_obj.delete()
    
def update_reaction(reaction_obj, reaction_type):
    reaction_obj.reaction = reaction_type
    reaction_obj.save()

def user_details(user_obj):
    user_details = {
        "user_id": user_obj.id,
        "name": user_obj.name,
        "profile_pic": user_obj.profile_pic 
    }
    return user_details
    
def comment_detials(comment_obj):
    return {
             "comment_id": comment_obj.id,
             "commenter":user_details(comment_obj.commented_by),
             "commented_at": strf_time_formating(comment_obj.commented_at),
             "comment_content": comment_obj.content,
             "reactions": {
                 "count": comment_obj.reaction.count(),
                 "type": list(dict.fromkeys([reaction.reaction for reaction in comment_obj.reaction.all()]))
            }
    }
    
def strf_time_formating(value):
    return value.strftime("%Y-%m-%d %H:%M:%S.%f")

    