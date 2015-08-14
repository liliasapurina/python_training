__author__ = '1'
from model.ab_group import Personal_data

def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.create(Personal_data(name="Maria",middlename="Olegovna",lastname="Vasnecova",nickname="OOMa",company="Pepsi",phone="345-55-66"))
    app.address.delete_first_address()