from django.db import models

class Blogger(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField()
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
