from selenium.webdriver.common.by import By
from selenium import webdriver


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").send_keys("%s" % username)
        self.driver.find_element(By.NAME, "pass").send_keys("%s" % password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

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
