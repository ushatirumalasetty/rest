from fb_post.models import Comment

from .validity import is_comment_valid

from .common_utils import strf_time_formating

def get_replies_for_comment(comment_id):# TODO : duplication of code
    is_comment_valid(comment_id)
    comments = Comment.objects\
    .filter(parent_comment_id=comment_id)\
    .select_related("commented_by")
    return [
                {
                    "comment_id": comment_obj.id,
                    "commenter":
                    {
                        "user_id": comment_obj.commented_by.id,
                        "name":  comment_obj.commented_by.name,
                        "profile_pic": comment_obj.commented_by.profile_pic
                    },
                    "commented_at": strf_time_formating(comment_obj.commented_at),
                    "comment_content": comment_obj.content
                }
                for comment_obj in comments
    ]
