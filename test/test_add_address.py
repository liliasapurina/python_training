# -*- coding: utf-8 -*-
from model.address import Address

def test_add_address(app, db, json_addresses):
    current_address = json_addresses
    old_addresses = db.get_address_list()
    app.address.create(current_address)
    new_addresses = db.get_address_list()
    old_addresses.append(current_address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
