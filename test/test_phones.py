__author__ = '1'

def test_phones_on_home_page(app):
    address_from_home_page = app.address.get_address_list()[0]
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.phone == address_from_edit_page.phone
    #assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone
    #assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    #assert contact_from_home_page.secondaryphone == contact_from_edit_page.secondaryphone