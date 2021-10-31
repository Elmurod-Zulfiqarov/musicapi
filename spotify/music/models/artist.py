from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    picture = models.URLField(blank=True)

    def __str__(self):
        return self.name

