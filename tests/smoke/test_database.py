from django.test import TestCase
from django.db import connections

class DatabaseTests(TestCase):
    def test_should_reach_the_database(self):
        default_connection = connections['default']
        try:
            cursor = default_connection.cursor() #this will take some time if error
        except OperationalError:
            reachable = False
        else:
            reachable = True
        self.assertTrue(reachable)
