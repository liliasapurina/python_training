# -*- coding: utf-8 -*-
from model.ab_group import Personal_data

def test_edit_first_address(app):
    app.session.login("admin", "secret")
    app.address.edit_first_address(Personal_data(name="Maria_edited",middlename="Olegovna_edited",lastname="Vasnecova_edited",nickname="OOMa_edited",company="Pepsi_edited",phone="345-55-66_edited"))
    app.session.logout()