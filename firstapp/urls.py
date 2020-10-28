from django.urls import path
from django.conf.urls import url
from firstapp import views
from .views import BlogListView, BlogDetailView, TagPostsView, AddPostView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    url(r'^posts/([\w-]+)/$', TagPostsView.as_view(), name='tag_posts'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    # path('hot/', .as_view(), name='hot_posts'),
    path('', BlogListView.as_view(), name='home'),
]