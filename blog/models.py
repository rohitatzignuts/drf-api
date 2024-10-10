from django.db import models


# Create your models here.
class Blog(models.Model):
    class BlogVisibility(models.TextChoices):
        PRIVATE = "PR", "Private"
        PUBLIC = "PU", "Public"

    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)
    banner = models.ImageField(default="f12024.webp", blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, default=None)
    visibility = models.CharField(
        max_length=2,
        choices=BlogVisibility.choices,
        default=BlogVisibility.PUBLIC,
    )
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):

    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.blog.title}"
