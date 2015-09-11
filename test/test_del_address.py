__author__ = '1'
from model.address import Address
import random

def test_delete_first_address(app, db):
    if len(db.get_address_list()) == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    old_addresses = db.get_address_list()
    address = random.choice(old_addresses)
    app.address.delete_address_by_id(address.id)
    assert len(old_addresses) - 1 == app.address.count()
    new_addresses = db.get_address_list()
    old_addresses.remove(address)
    assert old_addresses == new_addresses