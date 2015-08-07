# -*- coding: utf-8 -*-
__author__ = 'vden'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_page(self, name_page):
        wd = self.wd
        wd.find_element_by_link_text(name_page).click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://192.168.0.2/addressbook/index.php")

    def destroy(self):
        self.wd.quit()


