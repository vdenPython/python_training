# -*- coding: utf-8 -*-
__author__ = 'vden'

class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit"))>0):
            wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        #wd.get("http://192.168.0.2/addressbook/index.php")
        wd.get("http://localhost/addressbook/index.php")




