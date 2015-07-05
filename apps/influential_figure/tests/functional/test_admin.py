from selenium import webdriver

from django.test import LiveServerTestCase


def check_content_on_page(live_server, text):
    body = live_server.browser.find_element_by_tag_name('body')
    live_server.assertIn(text, body.text)


def login_as_admin(live_server, username, password):
    username_field = live_server.browser.find_element_by_name('username')
    username_field.send_keys(username)
    password_field = live_server.browser.find_element_by_name('password')
    password_field.send_keys(password)
    login_button = live_server.browser.find_element_by_xpath("//input[@value='Log in']")
    login_button.click()


def logout(live_server):
    user_drop_down = live_server.browser.find_element_by_xpath("//*[contains(text(), 'Welcome')]")
    user_drop_down.click()
    logout_link = live_server.browser.find_element_by_link_text('Log out')
    logout_link.click()


class AdminTest(LiveServerTestCase):

    fixtures = ['admin.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_admin_login_logout(self):
        self.browser.get(self.live_server_url + '/admin/')
        check_content_on_page(self, 'Nina administration')

        login_as_admin(self, 'nina', 'nina')
        check_content_on_page(self, 'Site administration')

        logout(self)
        check_content_on_page(self, 'Logged out')
