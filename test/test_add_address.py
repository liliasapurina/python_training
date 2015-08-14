# -*- coding: utf-8 -*-
from model.ab_group import Personal_data

def test_add_address(app):
    app.address.create(Personal_data(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
