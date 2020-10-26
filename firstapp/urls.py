from django.urls import path
from django.conf.urls import url
from firstapp import views
from .views import BlogListView, BlogDetailView, TagPostsView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    url(r'^posts/([\w-]+)/$', TagPostsView.as_view()),
    path('', BlogListView.as_view(), name='home'),
]