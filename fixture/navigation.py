# -*- coding: utf-8 -*-
__author__ = 'vden'

class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self, name_page):
        wd = self.app.wd
        wd.find_element_by_link_text(name_page).click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://192.168.0.2/addressbook/index.php")




