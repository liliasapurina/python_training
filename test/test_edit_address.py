# -*- coding: utf-8 -*-
from model.address import Address
from random import randrange

def test_edit_first_address_name(app, check_ui):
    if app.address.count() == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="3455566"))
    old_addresses = app.address.get_address_list()
    current_address = Address(name="Maria_edited")
    index = randrange(len(old_addresses))
    current_address.id = old_addresses[index].id
    app.address.edit_address_by_index(index, current_address)
    assert len(old_addresses) == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[index] = current_address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
    if check_ui:
        assert sorted(new_addresses, key = Address.id_or_max) == sorted(app.address.get_address_list(), key = Address.id_or_max)

