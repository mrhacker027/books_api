from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, related_name="books"
    )
    description = models.TextField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
