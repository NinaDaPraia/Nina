from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from apps.influential_figures.serializers import InfluentialFigureSerializer
from apps.influential_figures.models import InfluentialFigure


@api_view(('GET',))
def api_root(request, format=None):
    return Response({"status": "OK"})


class InfluentialListFigureView(ListCreateAPIView):
    serializer_class = InfluentialFigureSerializer

    queryset = InfluentialFigure.objects.all()


class InfluentialFigureView(RetrieveAPIView):
    queryset = InfluentialFigure.objects.all()
    lookup_field = 'id'
    serializer_class = InfluentialFigureSerializer
