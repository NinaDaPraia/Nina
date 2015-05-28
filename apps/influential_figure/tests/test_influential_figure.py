from rest_framework.test import APISimpleTestCase
from rest_framework import status

class InfluentialFigureTest(APISimpleTestCase):
    def test_get_influential_figure_list(self):
        response = self.client.get("/influential_figures")
        self.assertEquals(status.HTTP_200_OK, response.status_code)