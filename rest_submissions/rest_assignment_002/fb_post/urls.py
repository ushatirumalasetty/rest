from django.urls import path

from .views import *

urlpatterns = [
    path('post/', create_new_post),
    path('post/<int:post_id>/', get_new_post), 
    path('comment/<int:comment_id>/reply/create/', new_reply_to_comment),
    path('post/<int:post_id>/react/', new_react_to_post),
    path('comment/<int:comment_id>/react/', new_react_to_comment),
    path('post/<int:post_id>/delete/', new_delete_post),
    path('post/<int:post_id>/comment/create/', new_create_comment),
    ]