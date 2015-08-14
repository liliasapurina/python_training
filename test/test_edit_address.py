# -*- coding: utf-8 -*-
from model.ab_group import Personal_data

def test_edit_first_address_name(app):
    if app.address.count() == 0:
        app.address.create(Personal_data(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    app.address.edit_first_address(Personal_data(name="Maria_edited"))

def test_edit_first_address_company(app):
    if app.address.count() == 0:
        app.address.create(Personal_data(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    app.address.edit_first_address(Personal_data(company="Pepsi_edited"))