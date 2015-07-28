from django.contrib import admin
from apps.influential_figures.models import SocialMovement, InfluentialFigure


class InfluentialFigureAdmin(admin.ModelAdmin):
    filter_horizontal = ('social_movements',)

admin.site.register(InfluentialFigure, InfluentialFigureAdmin)
admin.site.register(SocialMovement)

admin.site.site_header = 'Nina administration'
