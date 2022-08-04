from selenium.webdriver.common.by import By

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).clear()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.app.open_home_page()
            self.contact_cache = []
            for row in self.app.driver.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        self.app.open_home_page()
        row = self.app.driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        self.app.open_home_page()
        row = self.app.driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        firstname = self.app.driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = self.app.driver.find_element(By.NAME, "lastname").get_attribute("value")
        id = self.app.driver.find_element(By.NAME, "id").get_attribute("value")
        homephone = self.app.driver.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = self.app.driver.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = self.app.driver.find_element(By.NAME, "work").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone)


