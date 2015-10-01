__author__ = '1'

from pytest_bdd import given, when, then
from model.address import Address
import random

@given('a address list')
def address_list(db):
    return db.get_address_list()

@given('a address with <name>,<nickname>,<lastname>,<middlename>')
def new_address(name,nickname,lastname,middlename):
    return Address(name=name,nickname=nickname,lastname=lastname,middlename=middlename)

@when('I add the address to the list')
def add_new_address(app, new_address):
    app.address.create(new_address)

@then('The new address list is equal to old list with the added address')
def verify_address_added(db, address_list, new_address):
    old_addresses = address_list
    new_addresses = db.get_address_list()
    old_addresses.append(new_address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)

@given('a non-empty address list')
def non_empty_address_list(app, db, new_address):
    if len(db.get_address_list()) == 0:
        app.address.create(new_address)
    return db.get_address_list()

@given('a random address from the list')
def random_address(non_empty_address_list):
    return random.choice(non_empty_address_list)

@when('I delete the address from the list')
def delete_address(app, random_address):
    app.address.delete_address_by_id(random_address.id)

@then('the new address list is equal old list without the deleted address')
def verify_address_deleted(db, non_empty_address_list, random_address):
    old_addresses = non_empty_address_list
    new_addresses = db.get_address_list()
    assert len(old_addresses) - 1 == len(new_addresses)
    old_addresses.remove(random_address)
    assert old_addresses == new_addresses

@given('a new values for address fields with <new_name>')
def new_address_values(new_name):
    return Address(name=new_name)

@when('I edit the address from the list')
def edit_address_value(app, db, new_address_value, non_empty_address_list):
    old_addresses = non_empty_address_list
    current_address = new_address_value
    address = random.choice(old_addresses)
    app.address.edit_address_by_id(address.id, current_address)

@then('the new address list is equal old list with edited feature values')
def verify_address_edited(app, db, non_empty_address_list, check_ui):
    old_addresses = non_empty_address_list
    assert len(old_addresses) == len(db.get_address_list())
    new_addresses = db.get_address_list()
    if check_ui:
        assert sorted(new_addresses, key = Address.id_or_max) == sorted(app.address.get_address_list(), key = Address.id_or_max)
