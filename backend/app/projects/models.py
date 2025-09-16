from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=96)
    tags = models.JSONField()
    links = models.JSONField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
