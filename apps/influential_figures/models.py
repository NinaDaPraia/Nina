from django.db import models


class SocialMovement(models.Model):
    name = models.TextField(unique=True)

    def __unicode__(self):
        return self.name


class InfluentialFigure(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()

    social_movements = models.ManyToManyField("SocialMovement")

    def __unicode__(self):
        return self.name
