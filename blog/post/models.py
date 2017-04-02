from django.db import models
from user_profile.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    content = models.TextField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    release_date = models.DateField()
    # post_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
