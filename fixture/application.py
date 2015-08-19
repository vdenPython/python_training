# -*- coding: utf-8 -*-
__author__ = 'vden'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper
from fixture.common import CommonHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)
        self.common = CommonHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()





