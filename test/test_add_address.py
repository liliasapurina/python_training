# -*- coding: utf-8 -*-
import pytest
from model.ab_group import Personal_data
from fixture.application import Application


@pytest.fixture
def app(request):
    # create fixture
    fixture = Application()
    # how to destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address(app):
    app.session.login("admin", "secret")
    app.address.create(Personal_data(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    app.session.logout()