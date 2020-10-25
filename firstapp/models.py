from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    # image?
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    tag = models.ManyToManyField('Tag', help_text="Select a tag for this book")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name