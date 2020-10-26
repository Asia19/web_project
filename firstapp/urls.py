from django.urls import path
from firstapp import views
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]