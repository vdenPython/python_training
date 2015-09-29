# -*- coding: utf-8 -*-
__author__ = 'vden'
from model.contact import Contact
import re


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
        self.app.common.change_field_value(field_name="home", text=contact.homephone)
        self.app.common.change_field_value(field_name="mobile", text=contact.mobilephone)
        self.app.common.change_field_value(field_name="work", text=contact.workphone)
        self.app.common.change_field_value(field_name="fax", text=contact.fax)
        self.app.common.change_field_value(field_name="address2", text=contact.address2)
        self.app.common.change_field_value(field_name="phone2", text=contact.seconderyphone)
        self.app.common.change_field_value(field_name="notes", text=contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector(".left>input[value='Delete").click()
        wd.switch_to_alert().accept()
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s'" % id).click()

    def modify_first_contact(self, new_contact_date):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_date):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_contact_by_index(index)
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
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_e_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  address=address, all_e_mails=all_e_mails,
                                                  all_phones_from_home_page = all_phones))
        return list(self.contact_cache)

    def get_contact_info_edit_page(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_contact_by_index(index)
        firstname = wd.find_element_by_name("lastname").get_attribute("value")
        lastname = wd.find_element_by_name("firstname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        seconderyphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, workphone=workphone,
                       email=email, email2=email2, email3=email3,
                       mobilephone=mobilephone, seconderyphone=seconderyphone )

    def get_contact_view_page(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        seconderyphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, seconderyphone=seconderyphone )