# -*- coding: utf-8 -*-
__author__ = 'vden'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper
from fixture.common import CommonHelper
import re
import random
import string


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

    def clear_contact(self, s):
        return re.sub("[( )-]", "",s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != " " ,
                                (map(lambda x: self.clear_contact(x),
                                     (filter(lambda x: x is not None,
                                             [contact.homephone, contact.mobilephone,
                                              contact.workphone, contact.seconderyphone]))))))







