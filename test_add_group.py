# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group

class TestAddnewgroup():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_add_group(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_groups_page()
    self.create_group(Group(name="ewewr", header="gsgdsfg", footer="sdfgdgfsd"))
    self.return_to_groups_page()
    self.logout()

  def test_add_empty_group(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_groups_page()
    self.create_group(Group(name="", header="", footer=""))
    self.return_to_groups_page()
    self.logout()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def return_to_groups_page(self):
    self.driver.find_element(By.LINK_TEXT, "group page").click()

  def create_group(self, group):
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

  def open_groups_page(self):
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def login(self, username, password):
    self.driver.find_element(By.NAME, "user").send_keys("%s" % username)
    self.driver.find_element(By.NAME, "pass").send_keys("%s" % password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_home_page(self):
    self.driver.get("http://localhost/addressbook/")
  
