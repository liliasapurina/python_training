__author__ = '1'
import re

def test_phones_on_home_page(app):
    address_from_home_page = app.address.get_address_list()[0]
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)

def test_phones_on_address_view_page(app):
    address_from_view_page = app.address.get_address_from_view_page(0)
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_view_page.all_fields == merge_fields_like_on_view_page(address_from_edit_page)

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(address):
   return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [address.phone, address.mobilephone, address.workphone, address.secondaryphone]))))

def merge_fields_like_on_view_page(address):
   return str(address.name)+" "+str(address.middlename)\
          +" "+str(address.lastname)+"\n"+str(address.nickname)\
          +"\n"+str(address.company)+"\n"+"\nH: "+str(address.phone)\
          +"\nM: "+str(address.mobilephone)+"\nW: "+str(address.workphone)\
          +"\n"+"\n"\
          +create_view_for_email(str(address.email))\
          +create_view_for_email(str(address.email2))\
          +create_view_for_email(str(address.email3))+'\n'\
          +"\nP: "+str(address.secondaryphone)

def create_view_for_email(email):
    if email != "":
        dog_index = email.find("@")
        return email+" (www."+email[dog_index+1:len(email)]+")"
    else:
        return "\n"