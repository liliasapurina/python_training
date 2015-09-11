__author__ = '1'
from model.group import Group
from model.address import Address

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_address_list(app, db):
    ui_list = app.address.get_address_list()
    def clean(address):
        return Address(id=address.id, name=address.name.strip(),lastname=address.lastname.strip())
    db_list = map(clean, db.get_address_list())
    assert sorted(ui_list, key=Address.id_or_max) == sorted(db_list, key=Address.id_or_max)
