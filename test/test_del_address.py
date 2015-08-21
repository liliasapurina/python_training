__author__ = '1'
from model.address import Address
from random import randrange

def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    old_addresses = app.address.get_address_list()
    index = randrange(len(old_addresses))
    app.address.delete_address_by_index(index)
    assert len(old_addresses) - 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[index:index + 1] = []
    assert old_addresses == new_addresses