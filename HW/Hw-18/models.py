from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

class Theme(models.Model):
    name = models.CharField(max_length=30)

class Poem(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)