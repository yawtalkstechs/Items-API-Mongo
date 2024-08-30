from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100 ,unique=True, blank=False)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, unique=True)

    def __str__(self):
        return f"{self.name}"

'''
class Entry(models.Model):
    item = models.EmbeddedField(
        model_container = Item,
    )
    headline = models.CharField(max_length=150)

'''