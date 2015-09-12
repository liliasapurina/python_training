__author__ = '1'
from fixture.db import DbFixture

db = DbFixture(host = "127.0.0.1", name = "addressbook", user = "root", password = "")

try:
    addresses = db.get_address_list()
    for address in addresses:
        print(address)
    print(len(addresses))
finally:
    db.destroy()