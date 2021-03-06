__author__ = '1'
from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group_data):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_data.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_data.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_data.footer)

    def create(self, group_data):
        wd = self.app.wd
        # open groups page
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_data)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_css_selector("div.msgbox").click()
        # return to groups page
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # open groups page
        self.open_group_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        # open groups page
        self.open_group_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def change_field_value(self,field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        # open groups page
        self.open_group_page()
        self.select_group_by_index(index)
        # submit edition
        wd.find_element_by_name("edit").click()
        # make editions
        self.change_field_value("group_name",new_group_data.name)
        self.change_field_value("group_header",new_group_data.header)
        self.change_field_value("group_footer",new_group_data.footer)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        # open groups page
        self.open_group_page()
        self.select_group_by_id(id)
        # submit edition
        wd.find_element_by_name("edit").click()
        # make editions
        self.change_field_value("group_name",new_group_data.name)
        self.change_field_value("group_header",new_group_data.header)
        self.change_field_value("group_footer",new_group_data.footer)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(0)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text,id=id))
        return list(self.group_cache)