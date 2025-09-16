from django.db import models


class Social(models.Model):
    name = models.CharField(max_length=64)
    fab_icon = models.CharField(max_length=64)
    link = models.TextField()

    def __str__(self):
        return self.name
