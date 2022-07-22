from time import timezone
from venv import create
from django.db import models
from django.utils import timezone


class Article(models.Model):
    STATUS = (
        ("d", "Draft"),
        ("p", "Published")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    descriptions = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS)
    
