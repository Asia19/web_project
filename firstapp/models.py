from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20, help_text="Enter a post tag")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    publication_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', help_text="Select a tag for this book")

    def __str__(self):
        return self.title