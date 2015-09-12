# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))
    old_groups = db.get_group_list()
    current_group = Group(name="My group_edited")
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group.id, current_group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
