from fb_post.models import Post

from .validity import is_user_valid, is_post_content_valid

import time

from django.db import connection

def timer(function):
    def wrapper(*args, **kwargs):
        before_time = time.time()
        result = function(*args, **kwargs)
        after_time = time.time()
        execution_time = after_time - before_time
        print("The execution of function time = {}".format(execution_time))
        return result
    return wrapper

def db_hits(function):
    def wrapper(*args,**kwargs):
        before_db_hits = len(connection.queries)
        result = function(*args, **kwargs)
        after_db_hits = len(connection.queries)
        total_db_hits = after_db_hits - before_db_hits
        print(total_db_hits)
        return result
    return wrapper



@timer
@db_hits
def create_post(user_id, post_content):
    is_post_content_valid(post_content)
    is_user_valid(user_id)

    new_post_obj = Post.objects.create(content=post_content, posted_by_id=user_id)
    new_post_obj_id = new_post_obj.id
    return new_post_obj
