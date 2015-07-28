from rest_framework.test import APISimpleTestCase
from rest_framework import status
from apps.influential_figure.tests import factories
from apps.influential_figure.tests.factories import InfluentialFigureFactory, InfluentialFigureResource


def login_as_user(api_test_case):
    new_user = factories.UserResource()
    api_test_case.client.post("/rest-auth/registration/", new_user)
    api_test_case.client.post("/rest-auth/login/", {
        'username': new_user['username'],
        'password': new_user['password1']
    })


class InfluentialFigureTest(APISimpleTestCase):
    def test_get_influential_figure_list(self):
        InfluentialFigureFactory()
        influential_figures = [
            {
                'name': 'Zumbi',
                'description': 'Zumbi dos Palmares',
                'image': 'image',
                'social_movements': []
            }
        ]

        response = self.client.get("/influential_figures")
        del response.data[0]['id']

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertDictEqual(influential_figures[0], response.data[0])

    def test_create_influential_figure(self):
        # TODO we should implement the social movements field and test it.
        influential_figure = InfluentialFigureResource()
        login_as_user(self)

        response = self.client.post("/influential_figures", influential_figure)
        del response.data['id']

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertDictEqual(influential_figure, response.data)

    def test_get_specific_influential_figure(self):
        influential_figure = InfluentialFigureFactory()
        expected_influential_figure = InfluentialFigureResource()

        response = self.client.get("/influential_figures/{}".format(influential_figure.id))
        del response.data['id']

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertDictEqual(expected_influential_figure, response.data)
