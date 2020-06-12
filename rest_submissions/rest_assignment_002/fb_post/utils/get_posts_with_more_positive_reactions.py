from django.db.models import Q, F, Count

from fb_post.models import Reaction

def get_posts_with_more_positive_reactions():
    positive_reactions = ["THUMBS-UP", "LIT","LOVE", "HAHA", "WOW"]
    negitive_reactions = ["SAD", "ANGRY", "THUMBS-DOWN"]

    positive_reactions_count = Count("reaction",
                                     filter=Q(reaction__in=positive_reactions))
    negitive_reactions_count = Count("reaction",
                                     filter=Q(reaction__in=negitive_reactions))

    list_of_post_ids_with_more_positive_reactions = Reaction.objects\
        .annotate(positive_reactions_count=positive_reactions_count)\
        .annotate(negitive_reactions_count=negitive_reactions_count)\
        .filter(positive_reactions_count__gt=F('negitive_reactions_count'))\
        .values_list("post_id", flat=True)\
        .distinct()

    return list_of_post_ids_with_more_positive_reactions
