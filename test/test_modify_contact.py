__author__ = 'vden'
from model.contact import Contact


def test_modify_first_contact_home(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(home="New home"))
    app.session.logout()

def test_modify_first_contact_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(title="New title"))
    app.session.logout()