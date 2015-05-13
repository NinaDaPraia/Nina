import requests
from flex.core import load, validate_api_call
from django.test import LiveServerTestCase

class TestApiRootContract(LiveServerTestCase):

    def test_should_satisfy_swagger_schema(self):
        schema = load('swagger.json')
        response = requests.get(self.live_server_url)
        try:
            validate_api_call(schema, raw_request=response.request, raw_response=response)
        except ValueError as e:
            message = e
            valid = False
        else:
            message = None
            valid = True

        self.assertTrue(valid, message)