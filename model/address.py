__author__ = '1'

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
        return "%s:%s" % (self.id,self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
