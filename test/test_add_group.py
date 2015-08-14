# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))


def test_add_empty_group(app):
    app.group.create(Group(name="",header="",footer=""))