# -*- coding: utf-8 -*-
from model.address import Address

def test_edit_first_address_name(app):
    if app.address.count() == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    old_addresses = app.address.get_address_list()
    current_address = Address(name="Maria_edited")
    current_address.id = old_addresses[0].id
    app.address.edit_first_address(current_address)
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)
    old_addresses[0] = current_address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)

#def test_edit_first_address_company(app):
#    if app.address.count() == 0:
#        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
#    old_addresses = app.address.get_address_list()
#    app.address.edit_first_address(Address(company="Pepsi_edited"))
#    new_addresses = app.address.get_address_list()
#    assert len(old_addresses) == len(new_addresses)