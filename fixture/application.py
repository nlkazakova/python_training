from selenium.webdriver.common.by import By
from selenium import webdriver

from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")


    def create_group(self, group):
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        # init group creation
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").send_keys("%s" % group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys("%s" % group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys("%s" % group.footer)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def destroy(self):
        self.driver.quit()
