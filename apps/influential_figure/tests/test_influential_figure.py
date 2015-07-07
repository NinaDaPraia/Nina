from rest_framework.test import APISimpleTestCase
from rest_framework import status

from apps.influential_figure.tests.factories import InfluentialFigureFactory


class InfluentialFigureTest(APISimpleTestCase):
    def test_get_influential_figure_list(self):
        InfluentialFigureFactory()
        influential_figures = [
            {
                'name': 'Zumbi',
                'description': 'Zumbi dos Palmares',
                'image': '',
                'social_movements': []
            }
        ]
        response = self.client.get("/influential_figures")
        del response.data[0]['id']
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(influential_figures, response.data)
