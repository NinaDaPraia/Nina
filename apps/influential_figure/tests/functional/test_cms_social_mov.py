from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

def login_as_admin(liveServer, username, password):
    liveServer.browser.get(liveServer.live_server_url + '/admin/')
    username_field = liveServer.browser.find_element_by_name('username')
    username_field.send_keys('nina')
    password_field = liveServer.browser.find_element_by_name('password')
    password_field.send_keys('nina')
    password_field.send_keys(Keys.RETURN)

class SocialMovementTest(LiveServerTestCase):

    fixtures = ['admin.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_create_sm(self):
        login_as_admin(self, 'nina', 'nina')
        expected_sm_name = 'SocialMovimentNameTest'

        add_sm_button = self.browser.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr/td[1]/a')
        add_sm_button.click()
        sm_name_field = self.browser.find_element_by_name('name')
        sm_name_field.send_keys(expected_sm_name)
        sm_save_button = self.browser.find_element_by_name('_save')
        sm_save_button.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('The social movement "' + expected_sm_name + '" was added successfully.', body.text)
