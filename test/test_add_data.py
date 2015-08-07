# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dfdfdfd", header="fdfdfdfd", footer="dfdfdfdfd"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="dffdfd", middlename="dfddfd", lastname="dfdfdfdf",
                               nickname="dfdfdfdf", title="dfdfdfdf", company="dfdfdfd",
                               address="dfdfdfdf", home="dfdfd", mobile="dfddfd", work="dfdfdf",
                               fax="dfddfd", address2="dfdfdfd", phone2="dfdfd", notes="dfddfd"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", title="", company="",
                               address="", home="", mobile="", work="",
                               fax="", address2="", phone2="", notes=""))
    app.session.logout()
