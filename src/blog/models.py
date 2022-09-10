from time import timezone

from django.db import models
from django.utils import timezone


class Article(models.Model):
    STATUS = (
        ("d", "Draft"),
        ("p", "Published")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self) -> str:
        return self.title
