from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=400)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True,blank=True, null = True)
