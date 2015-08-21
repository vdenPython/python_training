# -*- coding: utf-8 -*-
__author__ = 'vden'
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_add_new_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.open_add_new_page()
        self.contact_cache = None

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
        self.app.navigation.open_home_page()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_date):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(new_contact_date)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        wd = self.app.wd
        if self.contact_cache is None:
            self.app.navigation.open_home_page()
            trx = 1
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                trx = trx+1
                lastnametext = element.find_element_by_xpath(
                    "//div[1]/div[4]/form[2]/table/tbody/tr["+str(trx)+"]/td[2]").text
                firstnametext = element.find_element_by_xpath(
                    "//div[1]/div[4]/form[2]/table/tbody/tr["+str(trx)+"]/td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, lastname=lastnametext, firstname=firstnametext))
        return list(self.contact_cache)