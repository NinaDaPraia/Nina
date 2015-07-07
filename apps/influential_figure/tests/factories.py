import factory

from Nina.apps.influential_figure.models import InfluentialFigure


class InfluentialFigureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InfluentialFigure

    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = ''


class InfluentialFigureResource(factory.DictFactory):
    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = ''
