# -*- coding: utf-8 -*-
from model.ab_group import Personal_data

def test_edit_first_address_name(app):
    app.session.login("admin", "secret")
    app.address.edit_first_address(Personal_data(name="Maria_edited"))
    app.session.logout()

def test_edit_first_address_company(app):
    app.session.login("admin", "secret")
    app.address.edit_first_address(Personal_data(company="Pepsi_edited"))
    app.session.logout()