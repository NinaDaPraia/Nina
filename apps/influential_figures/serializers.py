from rest_framework.serializers import ModelSerializer, StringRelatedField
from apps.influential_figures.models import InfluentialFigure


class InfluentialFigureSerializer(ModelSerializer):
    social_movements = StringRelatedField(many=True)

    class Meta:
        model = InfluentialFigure
