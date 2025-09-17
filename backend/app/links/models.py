from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=64)
    fab_icon = models.CharField(max_length=64)
    url = models.TextField()

    def __str__(self):
        return self.name
