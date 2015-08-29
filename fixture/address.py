__author__ = '1'
from model.address import Address
import re

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def open_address_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            self.app.open_home_page()

    def fill_address_form(self, data):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(data.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(data.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(data.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(data.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(data.company)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(data.phone)

    def create(self, data):
        wd = self.app.wd
        # init adress creation
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(data)
        # submit adress creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_address_page()
        self.address_cache = None

    def select_address_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_address_by_index(self, index):
        wd = self.app.wd
        # open groups page
        self.open_address_page()
        self.select_address_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_address_page()
        self.address_cache = None

    def delete_first_address(self):
        self.delete_address_by_index(0)

    def change_field_value(self,field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_address_by_index(self,index):
        wd = self.app.wd
        # init adress creation
        return wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def edit_address_by_index(self, index, data):
        wd = self.app.wd
        # init adress creation
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        # fill form
        self.change_field_value("firstname",data.name)
        self.change_field_value("middlename",data.middlename)
        self.change_field_value("lastname",data.lastname)
        self.change_field_value("nickname",data.nickname)
        self.change_field_value("company",data.company)
        self.change_field_value("home",data.phone)
        # submit adress creation
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_address_page()
        self.address_cache = None

    def edit_first_address(self, data):
        self.edit_address_by_index(0)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.open_address_page()
            self.address_cache = []
            for element in wd.find_elements_by_xpath("//div[1]/div[4]/form[2]/table/tbody/tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                name = cells[2].text
                middlename = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.address_cache.append(Address(name=name, middlename=middlename, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.address_cache)

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_address_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        phone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Address(name=name, middlename=middlename,lastname=lastname, id=id,
                       company=company,nickname=nickname,
                       phone=phone, mobilephone=mobilephone,workphone=workphone,secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)

    def open_address_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_address_view_by_index(self, index):
        wd = self.app.wd
        self.open_address_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_address_from_view_page(self, index):
        wd = self.app.wd
        self.open_address_view_by_index(index)
        text = wd.find_element_by_id("content").text
        #phone = re.search("H: (.*)",text).group(1)
        #mobilephone = re.search("M: (.*)",text).group(1)
        #workphone = re.search("W: (.*)",text).group(1)
        #secondaryphone = re.search("F: (.*)",text).group(1)
        return Address(all_fields=text)