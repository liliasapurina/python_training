__author__ = '1'
import mysql.connector
from model.group import Group
from model.address import Address

class DbFixture:

    def __init__(self, host, user, name, password):
        self.host = host
        self.user = user
        self.name = name
        self.password = password
        self.connection = mysql.connector.connect(host = host, database = name, user = user, password = password)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def get_address_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id,firstname,middlename,lastname,nickname,company,email,email2,email3,mobile,work,home,phone2,address from addressbook")
            for row in cursor:
                (id,firstname,middlename,lastname,nickname,company,email,email2,email3,mobile,work,home,phone2,address) = row
                list.append(Address(id=str(id),name=firstname,middlename=middlename,lastname=lastname,
                                    nickname=nickname,company=company,email=email,email2=email2,email3=email3,
                                    mobilephone=mobile,workphone=work,phone=home,secondaryphone=phone2,
                                    address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()