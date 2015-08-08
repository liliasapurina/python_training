__author__ = '1'

import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    # create fixture
    fixture = Application()
    # how to destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture