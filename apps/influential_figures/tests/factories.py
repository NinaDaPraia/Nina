import factory
from apps.influential_figures.models import InfluentialFigure, SocialMovement


class SocialMovement(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialMovement

    name = factory.Sequence(lambda n: "Social Movements #%s" % n)


class InfluentialFigureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InfluentialFigure

    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = 'image'

    @factory.post_generation
    def social_movements(self, create, extracted):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.social_movements.add(group)


class InfluentialFigureResource(factory.DictFactory):
    name = 'Zumbi'
    description = 'Zumbi dos Palmares'
    image = 'image'
    social_movements = []
