__author__ = '1'
from sys import maxsize

class Address:
    def __init__(self,name = None,middlename = None,lastname = None,nickname = None,company = None,address=None,id = None,
                 phone = None,mobilephone = None,workphone = None,secondaryphone = None,
                 all_phones_from_home_page = None,all_fields = None,
                 email = None,email2 = None,email3 = None,all_emails_from_home_page=None):
        self.name = name
        self.phone = phone
        self.address = address
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_fields = all_fields
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page=all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id,self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.lastname == self.lastname

    def id_or_max(adr):
        if adr.id:
            return int(adr.id)
        else:
            return maxsize
