# -*- coding: utf-8 -*-
from model.address import Address

def test_edit_first_address_name(app):
    if app.address.count() == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    old_addresses = app.address.get_address_list()
    app.address.edit_first_address(Address(name="Maria_edited"))
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)

def test_edit_first_address_company(app):
    if app.address.count() == 0:
        app.address.create(Address(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    old_addresses = app.address.get_address_list()
    app.address.edit_first_address(Address(company="Pepsi_edited"))
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)