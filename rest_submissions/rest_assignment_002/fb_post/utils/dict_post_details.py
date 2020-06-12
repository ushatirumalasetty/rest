from datetime import datetime

from .common_utils import strf_time_formating, user_details, comment_detials

def replies_dict(reply_obj):
    replies_dict = comment_detials(reply_obj)
    return replies_dict

def comments_dict(comment_obj, reply_list):
    comments_dict= {
                "comment_id": comment_obj.id,
                "commenter":user_details(comment_obj.commented_by),
                "commented_at": strf_time_formating(comment_obj.commented_at),
                "comment_content": comment_obj.content,
                "reactions": {# TODO : duplication
                    "count": comment_obj.reaction.count(),
                    "type": list(dict.fromkeys([reaction.reaction for reaction in comment_obj.reaction.all()]))
                },
                "replies_count": len(reply_list),
                "replies": reply_list,
    }
    return comments_dict

def get_dict_details_of_post(post_obj):
    comment_list = []
    for comment_obj in post_obj.comments.all():
        reply_list = [
            replies_dict(reply_obj)
            for reply_obj in post_obj.comments.all()
            if reply_obj.parent_comment_id == comment_obj.id # TODO : 
        ]
        
        if not comment_obj.parent_comment_id:# TODO : encapuslation condition
            comment_list.append(comments_dict(comment_obj, reply_list))
    posts_dict = {
                   "post_id": post_obj.id,
                   "posted_by": user_details(post_obj.posted_by),
                   "posted_at": strf_time_formating(post_obj.posted_at),
                   "post_content": post_obj.content,
                   "reactions": {# TODO : 
                       "count": post_obj.reaction.count(),
                       "type": list(dict.fromkeys([reaction.reaction for reaction in post_obj.reaction.all()]))
                   },           
                   "comments" : comment_list,
                   "comments_count": len(comment_list),
    }
    return posts_dict
