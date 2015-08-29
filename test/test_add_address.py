# -*- coding: utf-8 -*-
from model.address import Address
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    symbols = string.digits + "-"*4 + "+" + "("*2 + ")"*2
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.digits + "-"*4 + "+" + "("*2 + ")"*2
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen/2))])+"@"+"".join([random.choice(symbols) for i in range(random.randrange(maxlen/2))])


testdata =[ Address(name="",lastname="",middlename="",nickname="",company="",phone="",mobilephone="",workphone="",secondaryphone="")] + [
    Address(name=random_string("name",10),lastname=random_string("lastname",10),middlename=random_string("middlename",10),
            nickname=random_string("nickname",10),company=random_string("company",10),
            phone=random_phone(10),mobilephone=random_phone(15),workphone=random_phone(10),secondaryphone=random_phone(15),
            email=random_email(20),email2=random_email(20),email3=random_email(20),
            address=random_string("address",20))
    for i in range(5)
]


@pytest.mark.parametrize("current_address",testdata,ids=[repr(x) for x in testdata])
def test_add_address(app, current_address):
    old_addresses = app.address.get_address_list()
    app.address.create(current_address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(current_address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
