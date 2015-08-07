# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="dfdfdfd", header="fdfdfdfd", footer="dfdfdfdfd"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="dffdfd", middlename="dfddfd", lastname="dfdfdfdf",
                               nickname="dfdfdfdf", title="dfdfdfdf", company="dfdfdfd",
                               address="dfdfdfdf", home="dfdfd", mobile="dfddfd", work="dfdfdf",
                               fax="dfddfd", address2="dfdfdfd", phone2="dfdfd", notes="dfddfd"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="",
                               nickname="", title="", company="",
                               address="", home="", mobile="", work="",
                               fax="", address2="", phone2="", notes=""))
    app.logout()
