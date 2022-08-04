import time

from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        if not (self.app.driver.current_url.endswith("/group.php")
                and len(self.app.driver.find_elements(By.NAME, "new")) > 0):
            self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.open_groups_page()
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()
        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        self.app.driver.find_element(By.NAME, "delete").click()
        self.group_cache = None

    def select_first_group(self):
        # select first group
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        # select first group
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        self.open_groups_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in self.app.driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                group_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))

        return list(self.group_cache)
