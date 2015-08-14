__author__ = '1'

import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app():
    global fixture
    if fixture is None:
        # create fixture
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin",password="secret")
    return fixture

@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    # how to destroy fixture
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture