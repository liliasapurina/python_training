# -*- coding: utf-8 -*-
from model.ab_group import Personal_data

def test_edit_first_address_name(app):
    app.address.edit_first_address(Personal_data(name="Maria_edited"))

def test_edit_first_address_company(app):
    app.address.edit_first_address(Personal_data(company="Pepsi_edited"))