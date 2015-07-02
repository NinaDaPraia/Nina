from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from django.test import LiveServerTestCase

def login_as_admin(liveServer, username, password):
    liveServer.browser.get(liveServer.live_server_url + '/admin/')
    username_field = liveServer.browser.find_element_by_name('username')
    username_field.send_keys('nina')
    password_field = liveServer.browser.find_element_by_name('password')
    password_field.send_keys('nina')
    password_field.send_keys(Keys.RETURN)

def create_social_moviment(liveServer, socialMovementName):
    social_movement_model_link = liveServer.browser.find_element_by_link_text('Social movements')
    social_movement_model_link.click()
    add_social_movement_link = liveServer.browser.find_element_by_link_text('Add social movement')
    add_social_movement_link.click()

    social_movement_name_field = liveServer.browser.find_element_by_name('name')
    social_movement_name_field.send_keys(socialMovementName)
    social_movement_save_button = liveServer.browser.find_element_by_name('_save')
    social_movement_save_button.click()

def create_influencial_figure(liveServer, name, socialMovement):
    influential_figure_model_link = liveServer.browser.find_element_by_link_text('Influential figures')
    influential_figure_model_link.click()
    add_influential_figure_link = liveServer.browser.find_element_by_link_text('Add influential figure')
    add_influential_figure_link.click()

    expected_influential_figure = 'Important Figure'
    name_field = liveServer.browser.find_element_by_name('name')
    name_field.send_keys(expected_influential_figure)
    description_field = liveServer.browser.find_element_by_name('description')
    description_field.send_keys('This is a very important person')
    image_field = liveServer.browser.find_element_by_name('image')
    image_field.send_keys('image_url')
    select = Select(liveServer.browser.find_element_by_name('social_movements'))
    select.select_by_visible_text(socialMovement)

    influential_figure_save_button = liveServer.browser.find_element_by_name('_save')
    influential_figure_save_button.click()

    body = liveServer.browser.find_element_by_tag_name('body')
    liveServer.assertIn('The influential figure "' + expected_influential_figure + '" was added successfully.', body.text)

class FiTest(LiveServerTestCase):

    fixtures = ['admin.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_create_influential_figure(self):
        login_as_admin(self, 'nina', 'nina')
        expected_social_movement = 'SocialMovimentTest'

        create_social_moviment(self, expected_social_movement)

        influential_figure_app_link = self.browser.find_element_by_link_text('Influential_Figure')
        influential_figure_app_link.click()

        create_influencial_figure(self, 'TestFigure', expected_social_movement)
