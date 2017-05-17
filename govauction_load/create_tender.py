#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from page_objects import *
from datetime import datetime
import unittest
import argparse

tender_id = None


class SeleniumMixin(unittest.TestCase):
    def assertlementIsPresentById(self, elem_id):
        try:
            self.driver.find_element_by_id(elem_id)
        except NoSuchElementException as error:
            self.fail(error)


class TestCreateTender(SeleniumMixin):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(broker['url'])
        self.driver.set_window_size(1200, 1000)
        self.login_page_owner = LoginPage(
            owner_users['email'], owner_users['password'], self.driver
        )
        self.create_tender_page = CreateTenderPage(self.driver)
        self.find_tender = FindTenderPage(self.driver)

    def test_create_tender(self):
        self.login_page_owner.login_as_owner()
        self.driver.get(create_tender_url)
        self.create_tender_page.create_tender()

        is_found = False
        for i in range(1, 10):
            try:
                given_tender_id = self.find_tender.get_tender_id()
                print given_tender_id
                if given_tender_id:
                    with open('load_results_create.txt', 'a') as f:
                        f.write(
                            'Tender_Owner created tender with {}, finished at {} ------------------ PASSED\n'.format(
                                given_tender_id, datetime.now())
                        )
                        f.close()
                is_found = True
                break
            except NoSuchElementException or UnicodeEncodeError:
                sleep(30)
                self.driver.refresh()
                self.driver.execute_script("window.scrollTo(0, 1582);")

                if not is_found:
                    with open('load_results_create.txt', 'a') as f:
                        f.write('Tender_Owner did NOT create tender, finished at {} ------------ FAILED\n'.format(
                            datetime.now())
                        )
                        f.close()
                    return False

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='create_tender')

    suite = unittest.TestSuite()
    suite.addTest(TestCreateTender("test_create_tender"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
