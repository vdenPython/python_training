# -*- coding: utf-8 -*-
__author__ = 'vden'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_page(name_page="add new")
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.common.change_field_value(field_name="firstname", text=contact.firstname)
        self.app.common.change_field_value(field_name="middlename", text=contact.middlename)
        self.app.common.change_field_value(field_name="lastname", text=contact.lastname)
        self.app.common.change_field_value(field_name="nickname", text=contact.nickname)
        self.app.common.change_field_value(field_name="title", text=contact.title)
        self.app.common.change_field_value(field_name="company", text=contact.company)
        self.app.common.change_field_value(field_name="address", text=contact.address)
        self.app.common.change_field_value(field_name="home", text=contact.home)
        self.app.common.change_field_value(field_name="mobile", text=contact.mobile)
        self.app.common.change_field_value(field_name="work", text=contact.work)
        self.app.common.change_field_value(field_name="fax", text=contact.fax)
        self.app.common.change_field_value(field_name="address2", text=contact.address2)
        self.app.common.change_field_value(field_name="phone2", text=contact.phone2)
        self.app.common.change_field_value(field_name="notes", text=contact.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

    def modify_first_contact(self, new_group_date):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(new_group_date)
        wd.find_element_by_name("update").click()