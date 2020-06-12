from fb_post.models import Reaction

from .validity import is_post_valid

from django.db.models import Count

def get_reaction_metrics(post_id):
    is_post_valid(post_id)

    reaction_metrices = Reaction.objects\
        .filter(post_id=post_id)\
        .values_list("reaction")\
    .annotate(Count("reaction"))

    return dict(reaction_metrices)
