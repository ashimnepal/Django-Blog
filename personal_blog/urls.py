from django.urls import path
from .views import post_detail,post_list,post_add,post_draft_list, draft_detail

urlpatterns = [
    path("", post_list),
    path("post-detail/<int:pk>/", post_detail),
    path("post-add/", post_add),
    path("draft-list/", post_draft_list),
    path("draft-detail/<int:pk>/", draft_detail),
    
]
