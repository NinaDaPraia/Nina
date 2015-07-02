from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

def login_as_admin(live_server, username, password):
    live_server.browser.get(live_server.live_server_url + '/admin/')
    username_field = live_server.browser.find_element_by_name('username')
    username_field.send_keys('nina')
    password_field = live_server.browser.find_element_by_name('password')
    password_field.send_keys('nina')
    password_field.send_keys(Keys.RETURN)

def create_social_movement(live_server, social_movement_name):
    enter_social_movement_model_button = live_server.browser.find_element_by_link_text('Social movements')
    enter_social_movement_model_button.click()
    add_social_movement_link = live_server.browser.find_element_by_link_text('Add social movement')
    add_social_movement_link.click()

    social_movement_name_field = live_server.browser.find_element_by_name('name')
    social_movement_name_field.send_keys(social_movement_name)
    social_movement_save_button = live_server.browser.find_element_by_name('_save')
    social_movement_save_button.click()

    body = live_server.browser.find_element_by_tag_name('body')
    live_server.assertIn('The social movement "' + social_movement_name + '" was added successfully.', body.text)

def update_social_movement(live_server, old_social_movement_name, new_social_movement_name):
    select_social_movement = live_server.browser.find_element_by_link_text(old_social_movement_name)
    select_social_movement.click()
    social_movement_name_field = live_server.browser.find_element_by_name('name')
    social_movement_name_field.clear()
    social_movement_name_field.send_keys(new_social_movement_name)
    social_movement_save_button = live_server.browser.find_element_by_name('_save')
    social_movement_save_button.click()

    body = live_server.browser.find_element_by_tag_name('body')
    live_server.assertIn('The social movement "' + new_social_movement_name + '" was changed successfully.', body.text)

def delete_social_movement(live_server, social_movement):
    select_social_movement = live_server.browser.find_element_by_link_text(social_movement)
    select_social_movement.click()
    delete_button = live_server.browser.find_element_by_link_text('Delete')
    delete_button.click()
    confirm_button = live_server.browser.find_element_by_xpath('//*[@id="content"]/form/div/input[2]')
    confirm_button.click()

    body = live_server.browser.find_element_by_tag_name('body')
    live_server.assertIn('The social movement "' + social_movement + '" was deleted successfully.', body.text)


class SocialMovementTest(LiveServerTestCase):

    fixtures = ['admin.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_create_sm(self):
        login_as_admin(self, 'nina', 'nina')
        expected_social_movement = 'SocialMovimentNameTest'

        create_social_movement(self, expected_social_movement)

        expected_social_movement_changed = 'SocialMovimentNameTestChanged'
        update_social_movement(self, expected_social_movement, expected_social_movement_changed)

        delete_social_movement(self, expected_social_movement_changed)
