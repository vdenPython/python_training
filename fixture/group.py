# -*- coding: utf-8 -*-
__author__ = 'vden'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
       wd = self.app.wd
       wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_page(name_page="groups")
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.app.common.change_field_value(field_name="group_name", text=group.name)
        self.app.common.change_field_value(field_name="group_header", text=group.header)
        self.app.common.change_field_value(field_name="group_footer", text=group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_page(name_page="groups")
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_date):
        wd = self.app.wd
        self.app.navigation.open_page(name_page="groups")
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_date)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

