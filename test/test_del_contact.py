# -*- coding: utf-8 -*-
__author__ = 'vden'
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_first_contact()
