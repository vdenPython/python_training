__author__ = 'vden'
from model.contact import Contact


def test_modify_first_contact_home(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_first_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
