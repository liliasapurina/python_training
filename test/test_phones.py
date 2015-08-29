__author__ = '1'
import re

def test_phones_on_home_page(app):
    address_from_home_page = app.address.get_address_list()[0]
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)

def test_phones_on_address_view_page(app):
    address_from_view_page = app.address.get_address_from_view_page(0)
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_view_page.phone == address_from_edit_page.phone
    assert address_from_view_page.mobilephone == address_from_edit_page.mobilephone
    assert address_from_view_page.workphone == address_from_edit_page.workphone
    assert address_from_view_page.secondaryphone == address_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(address):
   return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x), [address.phone, address.mobilephone, address.workphone, address.secondaryphone])))