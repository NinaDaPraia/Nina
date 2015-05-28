from django.db import models

class InfluentialFigure(models.Model):
    name = models.TextField()
    nationality = models.TextField()

