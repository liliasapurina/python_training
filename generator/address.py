__author__ = '1'

from model.address import Address
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f:",["number of groups","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/addresses.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
