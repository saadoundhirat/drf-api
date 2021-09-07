from django.contrib.auth import get_user_model
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title