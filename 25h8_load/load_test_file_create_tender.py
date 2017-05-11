from selenium import webdriver
import unittest
from page_objects import *
import subprocess


class SeleniumMixin(unittest.TestCase):
    def assertElementIsPresentById(self, elem_id):
        try:
            self.driver.find_element_by_id(elem_id)
        except NoSuchElementException as error:
            self.fail(error)


class TestCreateTender(SeleniumMixin):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page_owner = LoginPage(
            owner_users['email'],
            owner_users['password'],
            self.driver
        )
        self.create_tender_page = CreateTenderPage(self.driver)
        self.find_tender = FindTenderPage(self.driver)

    def test_create_15_tenders(self):
        for i in range(12):
            subprocess.Popen('python create_tender.py', shell=True)

if __name__ == '__main__':
    unittest.main()
