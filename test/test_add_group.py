# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    # create fixture
    fixture = Application()
    # how to destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture

           
def test_add_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="My group",header="Hello",footer="Lili4ka1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="",header="",footer=""))
    app.session.logout()