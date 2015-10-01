__author__ = '1'

from pytest_bdd import scenario
from .address_steps import *

@scenario('address.feature', 'Add new address')
def test_add_new_address():
    pass

@scenario('address.feature', 'Delete a address')
def test_delete_address():
    pass

@scenario('address.feature', 'Edit a address')
def test_edit_address():
    pass

