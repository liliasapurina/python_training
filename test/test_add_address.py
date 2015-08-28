# -*- coding: utf-8 -*-
from model.address import Address

def test_add_address(app):
    old_addresses = app.address.get_address_list()
    current_address = Address(name="Maria",lastname="Olegovna",middlename="Vasnecova",nickname="OOMa",company="Pepsi",phone="3455566")
    app.address.create(current_address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(current_address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
