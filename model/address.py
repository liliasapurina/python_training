__author__ = '1'
from sys import maxsize

class Address:
    def __init__(self,name = None,middlename = None,lastname = None,nickname = None,company = None,phone = None,id = None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.phone = phone
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id,self.name, self.middlename)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.middlename == self.middlename

    def id_or_max(adr):
        if adr.id:
            return int(adr.id)
        else:
            return maxsize
