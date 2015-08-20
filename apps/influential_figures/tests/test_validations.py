from rest_framework import status
from rest_framework.test import APISimpleTestCase
from apps.influential_figures.tests import factories


class InfluentialFigureValidationTest(APISimpleTestCase):
    def test_name_is_required(self):
        influential_figure = factories.InfluentialFigureResource()
        del influential_figure['name']

        response = self.client.post("/influential_figures", influential_figure)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals({'name': ['This field is required.']}, response.data)

    def test_description_is_required(self):
        influential_figure = factories.InfluentialFigureResource()
        del influential_figure['description']

        response = self.client.post("/influential_figures", influential_figure)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals({'description': ['This field is required.']}, response.data)

    def test_image_is_required(self):
        influential_figure = factories.InfluentialFigureResource()
        del influential_figure['image']

        response = self.client.post("/influential_figures", influential_figure)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals({'image': ['This field is required.']}, response.data)

    def test_social_movements_is_required(self):
        influential_figure = factories.InfluentialFigureResource()
        del influential_figure['image']

        response = self.client.post("/influential_figures", influential_figure)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals({'image': ['This field is required.']}, response.data)
