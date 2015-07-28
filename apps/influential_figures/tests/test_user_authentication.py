from rest_framework.test import APISimpleTestCase

from apps.influential_figures.tests.factories import UserResource


def create_user(api_test_case, user):
    response = api_test_case.client.post("/rest-auth/registration/", user)
    api_test_case.assertEquals(user['username'], response.data['username'])


def login_user(api_test_case, user):
    response = api_test_case.client.post("/rest-auth/login/", {
        'username': user['username'],
        'password': user['password1']
    })
    stored_user = api_test_case.client.get("/rest-auth/user/", {'token': response.data['key']})
    api_test_case.assertEquals(stored_user.data['username'], user['username'])


def update_user(api_test_case, user_created):
    updated_user = UserResource()
    response = api_test_case.client.put("/rest-auth/user/", updated_user)
    api_test_case.assertEquals(response.data['username'], updated_user['username'])


def logout(api_test_case):
    response = api_test_case.client.post("/rest-auth/logout/")
    api_test_case.assertTrue(response.data['success'], "Successfully logged out.")


class UserAuthenticationTest(APISimpleTestCase):
    def test_register_new_user(self):
        new_user = UserResource()
        create_user(self, new_user)
        login_user(self, new_user)
        update_user(self, new_user)
        logout(self)
