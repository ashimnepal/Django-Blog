from django.urls import path
from .views import post_delete, post_detail, post_edit,post_list,post_add,draft_list, draft_detail, post_publish

urlpatterns = [
    path("", post_list),
    path("post-detail/<int:pk>/", post_detail, name="post-detail"),
    path("post-add/", post_add, name="post-add"),
    path("draft-list/", draft_list,name="draft-list" ),
    path("draft-detail/<int:pk>/", draft_detail, name="draft-detail"),
    path("post-published/<int:pk>/", post_publish, name="post-published"),
    path("post-delete/<int:pk>/", post_delete, name="post-delete"),
    path("post-edit/<int:pk>/", post_edit, name="post-edit"),
    
]
