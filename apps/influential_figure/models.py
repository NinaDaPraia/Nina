from django.db import models

class SocialMovement(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class InfluentialFigure(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()

    social_movements = models.ManyToManyField("SocialMovement")
