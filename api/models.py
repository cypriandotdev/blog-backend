from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Series(models.Model):
    name = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True)
    series = models.ForeignKey(Series, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    hidden = models.BooleanField(default=True)
    tags = ArrayField(models.CharField(max_length=50))
    content = models.TextField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title 
