__author__ = '1'

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

    def select_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_address(self):
        wd = self.app.wd
        # open groups page
        self.open_address_page()
        self.select_first_address()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_address_page()

    def change_field_value(self,field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_address(self, data):
        wd = self.app.wd
        # init adress creation
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
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

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

