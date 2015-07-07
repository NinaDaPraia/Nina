import factory

from apps.influential_figure.models import InfluentialFigure


class InfluentialFigureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InfluentialFigure

    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = 'image'
    social_movements = []


class InfluentialFigureResource(factory.DictFactory):
    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = 'image'
    social_movements = []
