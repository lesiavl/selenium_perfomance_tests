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

    def login_as_provider(self):
        wait_until_visible(self.driver, login_button, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(login_button).click()
        wait_before_click(self.driver, username_field, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(username_field).send_keys(self.email)
        self.driver.find_element_by_css_selector(pass_field).send_keys(self.password)
        self.driver.find_element_by_css_selector(submit_login_button).click()


class CreateTenderPage:

    def __init__(self, driver):
        self.driver = driver

    def create_tender(self):

        self.driver.find_element_by_css_selector(input_title).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_css_selector(input_description).send_keys('LOAD_TEST_Below_Threshold')

        enquiry_start = service.time_service()[0]
        self.driver.find_element_by_css_selector(input_start_enquiry).send_keys(enquiry_start)

        enquiry_end = service.time_service()[1]
        self.driver.find_element_by_css_selector(input_end_enquiry).send_keys(enquiry_end)

        tender_start = service.time_service()[2]
        self.driver.find_element_by_css_selector(input_start_tender).send_keys(tender_start)

        tender_end = service.time_service()[3]
        self.driver.find_element_by_css_selector(input_end_tender).send_keys(tender_end)

        self.driver.find_element_by_css_selector(save_draft).click()
        wait_until_visible(self.driver, add_lot, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(add_lot).click()

        wait_until_visible(self.driver, input_lot_title, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(input_lot_title).send_keys('LOAD_TEST_Below_Threshold LOT')
        self.driver.find_element_by_css_selector(input_lot_description).send_keys('LOAD_TEST_Below_Threshold LOT')

        self.driver.execute_script("""$('#Value_Amount').data("kendoNumericTextBox").value('3000.00');""")
        # self.driver.find_element_by_css_selector(input_value_amount).send_keys('3000.00')
        self.driver.execute_script("""$('#MinimalStep_Amount').data("kendoNumericTextBox").value('30.00');""")

        self.driver.find_element_by_css_selector(save_draft2).click()
        self.driver.execute_script('location.href = "{}";'.format(add_item))
        wait_until_visible(self.driver, add_item, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(add_item).click()

        self.driver.find_element_by_css_selector(input_item_description).send_keys('LOAD_TEST_Below_Threshold ITEM')

        self.driver.find_element_by_css_selector(select_cpv).click()
        wait_until_visible(self.driver, select_cpv_1item, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_cpv_1item).click()
        wait_for_presence(self.driver, cpv_selected, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_cpv).click()

        self.driver.execute_script('location.href = "{}";'.format(select_unit))

        self.driver.find_element_by_css_selector(select_unit).click()
        wait_until_visible(self.driver, select_unit1, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_unit1).click()
        self.driver.find_element_by_css_selector(input_quantity).send_keys(10)

        self.driver.execute_script('location.href = "{}";'.format(input_delivery_start_date))
        delivery_start = service.time_service()[4]
        self.driver.find_element_by_css_selector(input_delivery_start_date).send_keys(delivery_start)

        delivery_end = service.time_service()[5]
        self.driver.find_element_by_css_selector(input_delivery_end_date).send_keys(delivery_end)

        self.driver.execute_script('location.href = "{}";'.format(input_delivery_address))
        wait_until_visible(self.driver, input_dropdown_region, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(input_dropdown_region).send_keys(u"Волинська область")

        self.driver.find_element_by_css_selector(input_postal_code).send_keys(02010)
        self.driver.find_element_by_css_selector(input_locality).send_keys(u"Ковель")
        self.driver.find_element_by_css_selector(input_delivery_address).send_keys("Random Valid Address, 7741")

        self.driver.find_element_by_css_selector(save_draft3).click()
        self.driver.execute_script('location.href = "{}";'.format(add_doc_button))
        self.driver.find_element_by_css_selector(add_doc_button).click()
        # self.driver.find_element_by_css_selector(doc_title).click()
        self.driver.find_element_by_css_selector(doc_title).send_keys("Tender Doc")

        file_to_upload = service.relative2absolute('./doc1.docx')
        self.driver.find_element_by_css_selector(doc_input).send_keys(file_to_upload)

        self.driver.find_element_by_css_selector(save_draft4).click()
        self.driver.execute_script('location.href = "{}";'.format(submit_create_tender))
        wait_until_visible(self.driver, submit_create_tender, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(submit_create_tender).click()


class FindTenderPage(CreateTenderPage):
    def get_tender_id(self):
        matched = False
        try:
            def find_id():
                sleep(5)
                self.driver.refresh()
                wait_until_visible(self.driver, tender_get_id_locator, select_type=By.CSS_SELECTOR)
                tender_id = self.driver.find_element_by_css_selector(tender_get_id_locator).text
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

        tender_id = self.driver.find_element_by_css_selector(tender_get_id_locator).text
        return tender_id

    def find_tender(self, id_tender):
        tender_id = id_tender
        wait_before_click(self.driver, select_search_type, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_search_type).click()

        wait_before_click(self.driver, input_search_field, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(input_search_field).send_keys(tender_id)
        self.driver.find_element_by_css_selector(search_tender_button).click()
        wait_until_visible(self.driver, select_tender, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_tender).click()
        return tender_id


class MakeBidPage:
    def __init__(self, driver):
        self.driver = driver

    def make_bid(self):

        wait_until_visible(self.driver, select_bids, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_bids).click()

        # "LOAD_TEST_Below_Threshold"
        is_found = False
        for i in range(1, 100):
            try:
                wait_until_visible(self.driver, make_bid_button, select_type=By.CSS_SELECTOR)
                self.driver.find_element_by_css_selector(make_bid_button).click()
                is_found = True
                break
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException):
                sleep(15)
                self.driver.refresh()

        if not is_found:
            return False

        wait_until_visible(self.driver, select_lot, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(select_lot).click()
        wait_until_visible(self.driver, input_bid_amount, select_type=By.XPATH)
        self.driver.execute_script("""$('input[id*="Value_Amount"]').data("kendoNumericTextBox").value("3000.00");""")
        file_to_upload = service.relative2absolute('./doc1.docx')
        self.driver.find_element_by_css_selector(input_bid_doc).send_keys(file_to_upload)

        return True

    def run_bid(self):
        wait_until_visible(self.driver, submit_bid_button, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(submit_bid_button).click()
        sleep(5)
        try:
            wait_for_presence(self.driver, delete_bid_button, select_type=By.CSS_SELECTOR)
            sleep(5)
        except TimeoutException as error:
            print(error)
            raise error

        return True
