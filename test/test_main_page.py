__author__ = 'vden'
from model.contact import Contact


def test_main_page(app, db):
    db_main_page_contacts = db.get_contact_list(True)
    app_main_page_contacts = app.contact.get_contact_list()
    assert sorted(db_main_page_contacts, key=Contact.id_or_max) == sorted(app_main_page_contacts, key=Contact.id_or_max)

