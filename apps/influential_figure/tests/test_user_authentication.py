from rest_framework.test import APISimpleTestCase
import json


def create_user(api_test_case, user):
    response = api_test_case.client.post("/rest-auth/registration/", user)
    data = json.loads(response.content)
    api_test_case.assertEquals(user['username'], data['username'])


def login_user(api_test_case, user):
    response = api_test_case.client.post("/rest-auth/login/", {
        'username': user['username'],
        'password': user['password1']
    })
    data = json.loads(response.content)
    stored_user = api_test_case.client.get("/rest-auth/user/", {'token': data['key']})
    stored_user = json.loads(stored_user.content)
    api_test_case.assertEquals(stored_user['username'], user['username'])


def update_user(api_test_case, user_created):
    updated_user = {
        'username': user_created['username'] + 'updated_name',
        'first_name': '',
        'last_name': '',
        'email': user_created['email']
    }
    response = api_test_case.client.put("/rest-auth/user/", updated_user)
    data = json.loads(response.content)
    api_test_case.assertEquals(data['username'], updated_user['username'])


def logout(api_test_case):
    response = api_test_case.client.post("/rest-auth/logout/")
    data = json.loads(response.content)
    api_test_case.assertTrue(data['success'], "Successfully logged out.")


class UserAuthenticationTest(APISimpleTestCase):
    def test_register_new_user(self):
        new_user = {
            'username': 'nina',
            'password1': 'ninanina',
            'password2': 'ninanina',
            'email': 'nina@gmail.com'
        }

        create_user(self, new_user)
        login_user(self, new_user)
        update_user(self, new_user)
        logout(self)
