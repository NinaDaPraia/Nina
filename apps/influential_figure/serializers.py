from rest_framework.serializers import ModelSerializer
from apps.influential_figure.models import InfluentialFigure

class InfluentialFigureSerializer(ModelSerializer):
    class Meta:
        model = InfluentialFigure