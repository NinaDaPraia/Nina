import factory
from apps.influential_figure.models import InfluentialFigure


class InfluentialFigureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InfluentialFigure

    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = 'image'


class InfluentialFigureResource(factory.DictFactory):
    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = 'image'
    social_movements = []


class UserResource(factory.DictFactory):
    username = factory.Sequence(lambda n: 'person{0}'.format(n))
    password1 = 'defaultpassword'
    password2 = 'defaultpassword'
    email = factory.Sequence(lambda n: 'person{0}@email.com'.format(n))
