# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    # create fixture
    fixture = Application()
    # how to destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture

           
def test_add_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name="My group",header="Hello",footer="Lili4ka1"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name="",header="",footer=""))
    app.logout()