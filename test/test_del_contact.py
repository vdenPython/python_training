# -*- coding: utf-8 -*-
__author__ = 'vden'

def test_delete_first_contact(app):
    app.contact.delete_first_contact()
