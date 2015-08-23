# -*- coding: utf-8 -*-
__author__ = 'vden'
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
       wd = self.app.wd
       wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.app.common.change_field_value(field_name="group_name", text=group.name)
        self.app.common.change_field_value(field_name="group_header", text=group.header)
        self.app.common.change_field_value(field_name="group_footer", text=group.footer)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_date):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_date):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_date)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        wd = self.app.wd
        if self.group_cache is None:
            self.app.navigation.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

