__author__ = '1'
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))
    app.group.delete_first_group()