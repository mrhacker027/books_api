from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
