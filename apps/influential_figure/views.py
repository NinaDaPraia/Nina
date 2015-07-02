from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from apps.influential_figure.serializers import InfluentialFigureSerializer
from apps.influential_figure.models import InfluentialFigure


@api_view(('GET',))
def api_root(request, format=None):
    return Response({"status": "OK"})


class InfluentialFigureView(ListAPIView):
    serializer_class = InfluentialFigureSerializer

    queryset = InfluentialFigure.objects.all()
