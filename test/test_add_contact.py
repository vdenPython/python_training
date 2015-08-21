# -*- coding: utf-8 -*-
__author__ = 'vden'
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="dffdfd", middlename="dfddfd", lastname="dfdfdfdf",
                      nickname="dfdfdfdf", title="dfdfdfdf", company="dfdfdfd",
                      address="dfdfdfdf", home="dfdfd", mobile="dfddfd", work="dfdfdf",
                      fax="dfddfd", address2="dfdfdfd", phone2="dfdfd", notes="dfddfd")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="",
                      nickname="", title="", company="",
                      address="", home="", mobile="", work="",
                      fax="", address2="", phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


