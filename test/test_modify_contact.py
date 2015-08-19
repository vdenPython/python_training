__author__ = 'vden'
from model.contact import Contact


def test_modify_first_contact_home(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(home="New home"))

def test_modify_first_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(title="New title"))
