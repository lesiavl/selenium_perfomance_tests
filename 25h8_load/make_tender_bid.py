#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from page_objects import *
import unittest
import argparse


tender_id = None
biduser = None
bidpassw = None


class SeleniumMixin(unittest.TestCase):
    def assertElementIsPresentById(self, elem_id):
        try:
            self.driver.find_element_by_id(elem_id)
        except NoSuchElementException as error:
            self.fail(error)


class MultipleProviders:

    def __init__(self, driver, user, passw):
        self.driver = driver
        self.user = user
        self.passw = passw

        self.login_page_provider = LoginPage(self.user, self.passw, self.driver)
        self.find_tender = FindTenderPage(self.driver)
        self.make_bid_page = MakeBidPage(self.driver)

    def mult_browsers_to_make_bid(self, tid):
        self.login_page_provider.login_as_provider()
        self.find_tender.find_tender(tid)
        return self.make_bid_page.make_bid()


class TestCreateTenderMakeBid(SeleniumMixin, MultipleProviders):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1200, 1000)
        self.driver.get(broker['url'])

    def test_create_tender_bid(self):
        make_bid_page = MultipleProviders(self.driver, biduser, bidpassw)

        if not make_bid_page.mult_browsers_to_make_bid(tender_id):
            with open('load_results.txt', 'a') as f:
                f.write('{} made bid for {} ------------ FAILED\n'.format(biduser, tender_id))
                f.close()
            self.fail('Failed since false')

        with open('load_results.txt', 'a') as f:
            f.write('{} made bid for {} ------------------ PASSED\n'.format(biduser, tender_id))
            f.close()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='make_tender_bid')
    parser.add_argument('--tenderid', type=str, help='tender id to find and make bid')
    parser.add_argument('--biduser', type=str, help='bid user')
    parser.add_argument('--bidpassw', type=str, help='bid passw')
    args = parser.parse_args()

    tender_id = args.tenderid
    biduser = args.biduser
    bidpassw = args.bidpassw

    suite = unittest.TestSuite()
    suite.addTest(TestCreateTenderMakeBid("test_create_tender_bid"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
