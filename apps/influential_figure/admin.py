from django.contrib import admin
from apps.influential_figure.models import SocialMovement, InfluentialFigure

# Register your models here.

admin.site.register(SocialMovement)


class InfluentialFigureAdmin(admin.ModelAdmin):
    filter_horizontal = ('social_movements',)

admin.site.register(InfluentialFigure, InfluentialFigureAdmin)

admin.site.site_header = 'Nina administration'
