__author__ = 'vden'
from fixture.db import Dbfixture

db = Dbfixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
   contacts = db.get_contact_list()
   for contact in contacts:
       print(contact)
   print(len(contacts))
finally:
    db.destroy()
