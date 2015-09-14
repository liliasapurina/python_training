# -*- coding: utf-8 -*-
from model.address import Address
import random

def test_edit_first_address_name(app, db, check_ui):
    if len(db.get_address_list()) == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="3455566"))
    old_addresses = db.get_address_list()
    current_address = Address(name="Maria_edited")
    address = random.choice(old_addresses)
    app.address.edit_address_by_id(address.id, current_address)
    assert len(old_addresses) == len(db.get_address_list())
    new_addresses = db.get_address_list()
    if check_ui:
        assert sorted(new_addresses, key = Address.id_or_max) == sorted(app.address.get_address_list(), key = Address.id_or_max)

