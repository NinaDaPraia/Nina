from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

def check_content_on_page(liveServer, text):
    body = liveServer.browser.find_element_by_tag_name('body')
    liveServer.assertIn(text, body.text)

def login_as_admin(liveServer, username, password):
    username_field = liveServer.browser.find_element_by_name('username')
    username_field.send_keys(username)
    password_field = liveServer.browser.find_element_by_name('password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

def logout(liveServer):
    logout_link = liveServer.browser.find_element_by_link_text('Log out')
    logout_link.click()

class AdminTest(LiveServerTestCase):

    fixtures = ['admin.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_admin_login_logout(self):
        self.browser.get(self.live_server_url + '/admin/')
        check_content_on_page(self, 'Django administration')

        login_as_admin(self, 'nina', 'nina')
        check_content_on_page(self, 'Site administration')

        logout(self)
        check_content_on_page(self, 'Logged out')
