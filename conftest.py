__author__ = '1'

import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseUrl = request.config.getoption("--baseUrl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser = browser, baseUrl = baseUrl)
    else:
        if not fixture.is_valid():
            fixture = Application(browser = browser, baseUrl = baseUrl)
    fixture.session.ensure_login(username = username,password = password)
    return fixture

@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    # how to destroy fixture
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="firefox")
    parser.addoption("--baseUrl",action="store",default="http://localhost/addressbook/")
    parser.addoption("--username",action="store",default="admin")
    parser.addoption("--password",action="store",default="secret")