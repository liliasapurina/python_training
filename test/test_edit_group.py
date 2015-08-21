# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))
    old_groups = app.group.get_group_list()
    current_group = Group(name="My edited group")
    index = randrange(len(old_groups))
    current_group.id = old_groups[index].id
    app.group.edit_group_by_index(index, current_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = current_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header="Hello, I'm edited"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
