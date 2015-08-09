# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin",password="secret")
    app.group.edit_first_group(Group(name="My edited group",header="Hello, I'm edited",footer="by Lili4ka Sapurina"))
    app.session.logout()

