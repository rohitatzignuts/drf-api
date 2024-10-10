from django.urls import path, include
from blog.views import BlogListCreate, BlogReadUpdateDelete

urlpatterns = [
    path("", BlogListCreate.as_view(), name="blog-list-create"),
    path(
        "<slug:slug>/", BlogReadUpdateDelete.as_view(), name="blog-read-update-delete"
    ),
]
