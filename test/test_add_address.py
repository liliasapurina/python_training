# -*- coding: utf-8 -*-
from model.address import Address
import pytest
from data.addresses import testdata

@pytest.mark.parametrize("current_address",testdata,ids=[repr(x) for x in testdata])
def test_add_address(app, current_address):
    old_addresses = app.address.get_address_list()
    app.address.create(current_address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(current_address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
