from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
    )
    tags = models.ManyToManyField(
        Tag,
    )
