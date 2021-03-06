# -*- coding: utf-8 -*-
__author__ = 'vden'
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, address2=None,
                 email=None, email2=None, email3=None, seconderyphone=None, notes=None,
                 id=None, all_phones_from_home_page=None, all_e_mails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.address2 = address2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.seconderyphone = seconderyphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_e_mails = all_e_mails

    def __repr__(self):
        return "%s,%s,%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id ) \
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize