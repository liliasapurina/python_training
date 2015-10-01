# -*- coding: utf-8 -*-
from model.group import Group
from model.address import Address
import random


def test_add_address_to_group(app, db, json_groups, json_addresses, check_ui):
    all_groups = db.get_group_list()
    current_group = random.choice(all_groups)
    current_address = json_addresses
    app.address.create(current_address)

    app.group.create(current_group)
    new_groups = db.get_group_list()
    old_groups.append(current_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)