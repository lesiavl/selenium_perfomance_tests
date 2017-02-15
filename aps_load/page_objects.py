#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from locators import *
from time import sleep
import service


def wait_before_click(driver, element):
    return ui.WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, element)))


def wait_until_visible(driver, element):
    return ui.WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, element)))


def wait_until_invisible(driver, element):
    return ui.WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.XPATH, element)))


def wait_for_presence(driver, element):
    return ui.WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, element)))


def wait_for_text_presence(driver, element, text):
    return ui.WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.XPATH, element), text))


class LoginPage:
    def __init__(self, email, password, driver):
        self.driver = driver
        self.email = email
        self.password = password

    def login_as_owner(self):
        wait_for_presence(self.driver, login_button)
        self.driver.find_element_by_xpath(login_button).click()
        self.driver.find_element_by_xpath(username_field).send_keys(self.email)
        self.driver.find_element_by_xpath(pass_field).send_keys(self.password)
        self.driver.find_element_by_xpath(submit_login_button).click()

    def login_as_provider(self):
        wait_for_presence(self.driver, login_button)
        self.driver.find_element_by_xpath(login_button).click()
        self.driver.find_element_by_xpath(username_field).send_keys(self.email)
        self.driver.find_element_by_xpath(pass_field).send_keys(self.password)
        self.driver.find_element_by_xpath(submit_login_button).click()


class CreateTenderPage:

    def __init__(self, driver):
        self.driver = driver

    def create_tender(self):
        wait_for_presence(self.driver, create_tender_button)
        self.driver.find_element_by_xpath(create_tender_button).click()

        wait_until_visible(self.driver, below_threshold_button)
        self.driver.find_element_by_xpath(below_threshold_button).click()
        self.driver.find_element_by_xpath(input_title).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_xpath(input_description).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_xpath(input_value_amount).send_keys(10000)
        self.driver.find_element_by_xpath(input_min_step).send_keys(100)

        self.driver.execute_script("window.scrollTo(0, 180);")
        self.driver.execute_script(input_start_enquiry)
        self.driver.execute_script(input_end_enquiry)

        self.driver.execute_script(input_start_tender)
        self.driver.execute_script(input_end_tender)
        wait_before_click(self.driver, '//*[@id="date_tender_end"]')
        self.driver.find_element_by_xpath('//*[@id="date_tender_end"]').click()
        self.driver.find_element_by_xpath(input_value_amount).click()

        wait_before_click(self.driver, next_button)
        self.driver.find_element_by_xpath(next_button).click()

        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, 749);")
        wait_for_presence(self.driver, add_item)
        self.driver.find_element_by_xpath(add_item).click()

        # self.driver.switch_to_alert().accept()
        wait_before_click(self.driver, input_item_description)
        self.driver.find_element_by_xpath(input_item_description).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_xpath(input_quantity).send_keys(10)
        self.driver.find_element_by_xpath(select_unit).click()
        self.driver.find_element_by_xpath(input_unit).send_keys(u'ящик')
        self.driver.find_element_by_xpath(select_unit_1).click()
        wait_until_invisible(self.driver, select_unit_1)

        self.driver.find_element_by_xpath(click_cpv_button).click()
        wait_until_visible(self.driver, select_cpv_1item)
        self.driver.find_element_by_xpath(select_cpv_1item).click()
        self.driver.find_element_by_xpath(confirm_cpv).click()

        self.driver.find_element_by_xpath(select_dkpp).click()
        wait_until_visible(self.driver, select_dkpp_1item)
        self.driver.find_element_by_xpath(select_dkpp_1item).click()
        self.driver.find_element_by_xpath(confirm_dkpp).click()

        self.driver.execute_script(input_delivery_start)
        self.driver.execute_script(input_delivery_end)

        wait_before_click(self.driver, delivery_checkbox)
        self.driver.find_element_by_xpath(delivery_checkbox).click()
        modal = self.driver.find_element_by_xpath('//*[@id="HideShow_div"]')
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", modal)

        self.driver.find_element_by_xpath(click_dropdown_country).click()
        self.driver.find_element_by_xpath(select_country).click()
        wait_until_invisible(self.driver, select_country)

        self.driver.find_element_by_xpath(click_dropdown_region).click()
        wait_for_presence(self.driver, input_region)
        self.driver.find_element_by_xpath(input_region).send_keys(u"м. Київ")
        self.driver.find_element_by_xpath(select_region).click()
        wait_until_invisible(self.driver, select_region)

        wait_before_click(self.driver, input_postal_code)
        self.driver.find_element_by_xpath(input_postal_code).click()
        self.driver.find_element_by_xpath(input_postal_code).send_keys(11111)
        self.driver.find_element_by_xpath(input_locality).send_keys(u'Київ')
        self.driver.find_element_by_xpath(input_delivery_address).send_keys('Some street 10')

        self.driver.find_element_by_xpath(input_latitude).send_keys('50.15')
        self.driver.find_element_by_xpath(input_longitude).send_keys('50.10')
        self.driver.find_element_by_xpath(input_height).send_keys('0')

        try:
            wait_until_visible(self.driver, save_changes)
            self.driver.find_element_by_xpath(save_changes).click()
        except NoSuchElementException:
            sleep(1)
            self.driver.find_element_by_xpath(save_changes).click()

        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, 730);")
        wait_until_visible(self.driver, add_tender_doc)
        self.driver.find_element_by_xpath(add_tender_doc).click()
        wait_until_visible(self.driver, select_type)
        self.driver.find_element_by_xpath(select_type).click()
        self.driver.find_element_by_xpath(select_doc_type).click()
        file_to_upload = service.relative2absolute('./Doc1.docx')
        self.driver.find_element_by_xpath(file_input).send_keys(file_to_upload)
        self.driver.find_element_by_xpath(submit_tender_doc_upload).click()

        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, 730);")
        wait_until_visible(self.driver, create_tender_draft)
        self.driver.find_element_by_xpath(create_tender_draft).click()

        wait_until_visible(self.driver, submit_create_tender)
        self.driver.find_element_by_xpath(submit_create_tender).click()

        wait_until_visible(self.driver, submit_popup)
        self.driver.find_element_by_xpath(decline_electr_signature).click()
        self.driver.find_element_by_xpath(submit_popup).click()


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
        wait_for_presence(self.driver, input_search_field)
        self.driver.find_element_by_xpath(input_search_field).send_keys(tender_id)
        self.driver.find_element_by_xpath(search_tender_button).click()
        wait_until_visible(self.driver, select_tender)
        self.driver.find_element_by_xpath(select_tender).click()
        return tender_id


class MakeBidPage:
    def __init__(self, driver):
        self.driver = driver

    def make_bid(self):

        is_found = False
        for i in range(1, 100):
            try:
                wait_for_presence(self.driver, all_bids)
                is_found = True
                break
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException):
                sleep(15)
                self.driver.refresh()

        if not is_found:
            return False

        self.driver.find_element_by_xpath(all_bids).click()
        self.driver.find_element_by_xpath(input_bid_amount).send_keys(10000)
        file_to_upload = service.relative2absolute('./Doc1.docx')
        self.driver.find_element_by_xpath(input_bid_doc).send_keys(file_to_upload)
        self.driver.find_element_by_xpath(submit_bid_doc).click()

        wait_until_visible(self.driver, submit_bid_button)
        return True

    def run_bid(self):
        sleep(3)
        self.driver.find_element_by_xpath(submit_bid_button).click()
        sleep(5)
        try:
            wait_for_presence(self.driver, delete_bid_button)
            sleep(5)
        except TimeoutException as error:
            print(error)
            raise error

        return True


