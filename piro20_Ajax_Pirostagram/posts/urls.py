from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path("", post_list, name="list"),
    path("create/", post_create, name="create"),
    path("like/", post_like, name="like"),
    path("comment/", post_comment, name="comment"),
    path("comment_delete/", comment_delete, name="comment_delete"),
    path("post_delete/", post_delete, name="post_delete"),
]