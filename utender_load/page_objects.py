#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from locators import *
from time import sleep
import service


def wait_before_click(driver, element, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((select_type, element)))


def wait_until_visible(driver, element, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((select_type, element)))


def wait_until_invisible(driver, element, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((select_type, element)))


def wait_for_presence(driver, element, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((select_type, element)))


def wait_for_text_presence(driver, element, text, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((select_type, element), text))


class LoginPage:
    def __init__(self, email, password, driver):
        self.driver = driver
        self.email = email
        self.password = password

    def login_as_owner(self):
        wait_until_visible(self.driver, login_button, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(login_button).click()
        wait_before_click(self.driver, username_field, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(username_field).send_keys(self.email)
        self.driver.find_element_by_css_selector(pass_field).send_keys(self.password)
        self.driver.find_element_by_css_selector(submit_login_button).click()
        wait_before_click(self.driver, close_notification, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(close_notification).click()
        wait_until_invisible(self.driver, close_notification, select_type=By.CSS_SELECTOR)

    def login_as_provider(self):
        wait_until_visible(self.driver, login_button, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(login_button).click()
        wait_before_click(self.driver, username_field, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(username_field).send_keys(self.email)
        self.driver.find_element_by_css_selector(pass_field).send_keys(self.password)
        self.driver.find_element_by_css_selector(submit_login_button).click()
        try:
            sleep(1)
            wait_until_visible(self.driver, close_notification, select_type=By.CSS_SELECTOR)
            self.driver.find_element_by_css_selector(close_notification).click()
            wait_until_invisible(self.driver, close_notification, select_type=By.CSS_SELECTOR)
            sleep(2)
        except TimeoutException:
            pass


class CreateTenderPage:

    def __init__(self, driver):
        self.driver = driver

    def create_tender(self):

        self.driver.execute_script("window.scrollTo(0, 730);")
        sleep(1)
        wait_before_click(self.driver, input_value_amount, select_type=By.CSS_SELECTOR)
        sleep(4)
        self.driver.find_element_by_css_selector(input_value_amount).send_keys(10000)
        self.driver.find_element_by_css_selector(input_min_step).send_keys(100)
        self.driver.execute_script("window.scrollTo(0, 1601);")
        self.driver.find_element_by_css_selector(input_title).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_css_selector(input_description).send_keys('LOAD_TEST_Below_Threshold')

        file_to_upload = service.relative2absolute('./doc1.docx')
        self.driver.find_element_by_xpath(add_doc).send_keys(file_to_upload)

        wait_until_visible(self.driver, input_item_description, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(input_item_description).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_css_selector(input_quantity).send_keys(10)

        self.driver.execute_script("window.scrollTo(0, 2214);")

        self.driver.find_element_by_css_selector(select_cpv).click()
        wait_until_visible(self.driver, select_cpv_1item, select_type=By.XPATH)
        self.driver.find_element_by_xpath(select_cpv_1item).click()
        wait_for_presence(self.driver, confirm_cpv, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(confirm_cpv).click()

        self.driver.execute_script("window.scrollTo(0, 2926);")
        wait_until_visible(self.driver, select_country, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_country).click()
        wait_until_visible(self.driver, select_dropdown_region, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_dropdown_region).click()

        self.driver.find_element_by_css_selector(input_locality).send_keys(u"Ковель")
        self.driver.find_element_by_css_selector(input_delivery_address).send_keys("Random Valid Address, 7741")
        self.driver.find_element_by_css_selector(input_postal_code).send_keys('02010')

        self.driver.execute_script("window.scrollTo(0, 3509);")
        self.driver.find_element_by_css_selector(input_delivery_start_date).click()
        self.driver.find_element_by_css_selector(input_delivery_start_date).clear()
        delivery_start = service.time_service()[3]
        wait_until_visible(self.driver, input_delivery_start_date, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(input_delivery_start_date).send_keys(delivery_start)

        self.driver.find_element_by_css_selector(input_delivery_end_date).click()
        self.driver.find_element_by_css_selector(input_delivery_end_date).clear()
        delivery_end = service.time_service()[4]
        self.driver.find_element_by_css_selector(input_delivery_end_date).send_keys(delivery_end)

        self.driver.execute_script("window.scrollTo(0, 3999);")
        self.driver.find_element_by_css_selector(input_end_enquiry).click()
        self.driver.find_element_by_css_selector(input_end_enquiry).clear()
        enquiry_end = service.time_service()[0]
        self.driver.find_element_by_css_selector(input_end_enquiry).send_keys(enquiry_end)

        self.driver.find_element_by_css_selector(input_start_tender).click()
        self.driver.find_element_by_css_selector(input_start_tender).clear()
        tender_start = service.time_service()[1]
        self.driver.find_element_by_css_selector(input_start_tender).send_keys(tender_start)

        self.driver.find_element_by_css_selector(input_end_tender).click()
        self.driver.find_element_by_css_selector(input_end_tender).clear()
        tender_end = service.time_service()[2]
        self.driver.find_element_by_css_selector(input_end_tender).send_keys(tender_end)

        self.driver.find_element_by_css_selector(input_procuring_entity).click()

        self.driver.execute_script("window.scrollTo(0, 4641);")
        wait_until_visible(self.driver, submit_create_tender, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(submit_create_tender).click()


class FindTenderPage(CreateTenderPage):
    def get_tender_id(self):
        matched = False
        try:
            def find_id():
                sleep(5)
                self.driver.refresh()
                wait_until_visible(self.driver, tender_get_id_locator)
                tender_id = self.driver.find_element_by_xpath(tender_get_id_locator).text
                matched = True
                return tender_id

            # Sometimes we need to wait for it
            while not matched:
                sleep(5)
                self.driver.refresh()
                tender_id = find_id()
                break

        except TimeoutException:
            self.driver.close()

        tender_id = self.driver.find_element_by_xpath(tender_get_id_locator).text
        return tender_id

    def find_tender(self, id_tender):
        tender_id = id_tender

        self.driver.get(tenders_list)
        wait_before_click(self.driver, input_search_field, select_type=By.CSS_SELECTOR)
        sleep(3)
        self.driver.find_element_by_css_selector(input_search_field).click()
        self.driver.find_element_by_css_selector(input_search_field).send_keys(tender_id)
        self.driver.find_element_by_css_selector(search_tender_button).click()
        sleep(5)
        wait_for_presence(self.driver, select_tender, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_tender).click()
        return tender_id


class MakeBidPage:
    def __init__(self, driver):
        self.driver = driver

    def make_bid(self):

# "LOAD_TEST_Below_Threshold"
        is_found = False
        for i in range(1, 100):
            try:
                wait_until_visible(self.driver, input_bid_amount, select_type=By.CSS_SELECTOR)
                self.driver.find_element_by_css_selector(input_bid_amount).click()
                is_found = True
                break
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException):
                sleep(15)
                self.driver.refresh()
                self.driver.execute_script("window.scrollTo(0, 3238);")

        if not is_found:
            return False

        self.driver.execute_script("window.scrollTo(0, 3238);")
        self.driver.find_element_by_css_selector(input_bid_amount).send_keys(10000)
        wait_until_visible(self.driver, submit_bid_button, select_type=By.CSS_SELECTOR)
        file_to_upload = service.relative2absolute('./doc1.docx')
        self.driver.find_element_by_xpath(add_doc).send_keys(file_to_upload)

        return True

    def run_bid(self):
        sleep(3)
        self.driver.find_element_by_css_selector(submit_bid_button).click()
        sleep(5)
        try:
            wait_for_presence(self.driver, assert_bid, select_type=By.CSS_SELECTOR)
            sleep(5)
        except TimeoutException as error:
            print(error)
            raise error

        return True
