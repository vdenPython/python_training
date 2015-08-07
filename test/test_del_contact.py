# -*- coding: utf-8 -*-
__author__ = 'vden'

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
