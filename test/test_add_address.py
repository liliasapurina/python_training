# -*- coding: utf-8 -*-
from model.address import Address

def test_add_address(app):
    old_addresses = app.address.get_address_list()
    app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) + 1 == len(new_addresses)
