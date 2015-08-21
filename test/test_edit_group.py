# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="My edited group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="Hello, I'm edited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
