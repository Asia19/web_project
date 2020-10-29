from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, help_text="Enter a post tag")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', help_text="Select a tag for this post")
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
        # return reverse('home')

    def total_likes(self):
        return self.likes.count()