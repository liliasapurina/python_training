__author__ = '1'
from model.address import Address

def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    old_addresses = app.address.get_address_list()
    app.address.delete_first_address()
    assert len(old_addresses) - 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[0:1] = []
    assert old_addresses == new_addresses