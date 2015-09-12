__author__ = '1'
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.address import Address
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column = "group_id")
        name = Optional(str, column = "group_name")
        header = Optional(str, column = "group_header")
        footer = Optional(str, column = "group_footer")

    class ORMAddress(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column = "id")
        name = Optional(str, column = "firstname")
        lastname = Optional(str, column = "lastname")
        email = Optional(str, column = "email")
        email2 = Optional(str, column = "email2")
        email3 = Optional(str, column = "email3")
        mobilephone = Optional(str, column = "mobile")
        workphone = Optional(str, column = "work")
        phone = Optional(str, column = "home")
        secondaryphone = Optional(str, column = "phone2")
        address = Optional(str, column = "address")
        deprecated = Optional(datetime, column = "deprecated")


    def __init__(self, host, user, name, password):
        self.db.bind('mysql', host = host, database = name, user = user, password = password, conv = decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            Group(id = str(group.id), name = group.name, header = group.header, footer = group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_addresses_to_model(self, addresses):
        def convert(address):
            Address(id = str(address.id), name = address.name, lastname = address.lastname,
                    email = address.email,email2 = address.email2, email3 = address.email3,
                    mobilephone = address.mobilephone, workphone = address.workphone, phone = address.phone, secondaryphone = address.secondaryphone,
                    address = address.address)
        return list(map(convert, addresses))

    @db_session
    def get_address_list(self):
        return self.convert_addresses_to_model(select(a for a in ORMFixture.ORMAddress if a.deprecated is None))