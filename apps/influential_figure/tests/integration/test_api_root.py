from django.test import Client, TestCase

class TestApiRoot(TestCase):
    def setUp(self):
        self.client = Client()

    def test_should_respond_with_status_ok(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)
    
    def test_should_respond_with_status_not_found(self):
        response = self.client.get("/not_found")
        self.assertEquals(response.status_code, 404)