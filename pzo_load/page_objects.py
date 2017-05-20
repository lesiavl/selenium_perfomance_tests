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
    return ui.WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((select_type, element)))


def wait_until_visible(driver, element, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((select_type, element)))


def wait_until_invisible(driver, element, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((select_type, element)))


def wait_for_presence(driver, element, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((select_type, element)))


def wait_for_text_presence(driver, element, text, select_type=By.XPATH):
    return ui.WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((select_type, element), text))


# def close_notif(driver):
#     for i in range(1):
#         try:
#             wait_until_visible(driver, close_notification, select_type=By.CSS_SELECTOR)
#             close_notif = driver.find_element_by_css_selector(close_notification)
#             sleep(2)
#             if close_notif.is_displayed():
#                 sleep(1)
#                 wait_before_click(driver, close_notification, select_type=By.CSS_SELECTOR)
#                 driver.find_element_by_css_selector(close_notification).click()
#             else:
#                 return False
#         except TimeoutException:
#             break


class LoginPage:
    def __init__(self, email, password, driver):
        self.driver = driver
        self.email = email
        self.password = password

    def login_as_owner(self):

        wait_before_click(self.driver, username_field, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(username_field).send_keys(self.email)
        self.driver.find_element_by_css_selector(pass_field).send_keys(self.password)
        self.driver.find_element_by_css_selector(submit_login_button).click()
        wait_until_invisible(self.driver, login_verif, select_type=By.CSS_SELECTOR)

        wait_until_visible(self.driver, ukr, select_type=By.XPATH)
        self.driver.find_element_by_xpath(ukr).click()

    def login_as_provider(self):

        wait_before_click(self.driver, username_field, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(username_field).send_keys(self.email)
        self.driver.find_element_by_css_selector(pass_field).send_keys(self.password)
        self.driver.find_element_by_css_selector(submit_login_button).click()
        wait_until_invisible(self.driver, submit_login_button, select_type=By.CSS_SELECTOR)

        wait_until_visible(self.driver, ukr, select_type=By.XPATH)
        self.driver.find_element_by_xpath(ukr).click()
        sleep(1)


class CreateTenderPage:

    def __init__(self, driver):
        self.driver = driver

    def create_tender(self):

        self.driver.get(create_tender_url)
        wait_until_visible(self.driver, input_title, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(input_title).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_css_selector(input_description).send_keys('LOAD_TEST_Below_Threshold')

        self.driver.execute_script("window.scrollTo(0, 442);")
        self.driver.execute_script(input_start_enquiry)
        self.driver.execute_script(input_end_enquiry)
        self.driver.execute_script(input_start_tender)
        self.driver.execute_script(input_end_tender)

        self.driver.find_element_by_css_selector(acceleration_on).click()
        self.driver.find_element_by_css_selector(step1_button).click()

        self.driver.execute_script("window.scrollTo(0, 161);")

        wait_until_visible(self.driver, input_lot_title, select_type=By.XPATH)
        self.driver.find_element_by_xpath(input_lot_title).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_xpath(input_lot_description).send_keys('LOAD_TEST_Below_Threshold')

        self.driver.find_element_by_xpath(input_value_amount).send_keys(3000)
        self.driver.find_element_by_xpath(input_min_step).send_keys(30)

        self.driver.execute_script("window.scrollTo(0, 720);")

        wait_until_visible(self.driver, input_item_description, select_type=By.XPATH)
        self.driver.find_element_by_xpath(input_item_description).send_keys('LOAD_TEST_Below_Threshold')
        self.driver.find_element_by_xpath(input_quantity).send_keys(10)

        self.driver.find_element_by_xpath(select_cpv).click()
        wait_until_visible(self.driver, select_cpv_1item, select_type=By.XPATH)
        self.driver.find_element_by_xpath(select_cpv_1item).click()
        wait_for_presence(self.driver, confirm_cpv, select_type=By.XPATH)
        self.driver.find_element_by_xpath(confirm_cpv).click()

        sleep(3)
        self.driver.find_element_by_xpath(click_delivery_checkbox).click()

        self.driver.execute_script("window.scrollTo(0, 986);")
        self.driver.find_element_by_xpath(click_dropdown_region).click()
        wait_until_visible(self.driver, select_region, select_type=By.XPATH)

        self.driver.find_element_by_xpath(input_postal_code).send_keys('02010')
        self.driver.find_element_by_xpath(input_locality).send_keys(u"Київ")
        self.driver.find_element_by_xpath(input_delivery_address).send_keys("Random Valid Address, 7741")

        self.driver.find_element_by_xpath(input_delivery_start_date).click()
        self.driver.find_element_by_xpath(input_delivery_start_date).clear()
        delivery_start = service.time_service()[4]
        wait_until_visible(self.driver, input_delivery_start_date, select_type=By.XPATH)
        self.driver.find_element_by_xpath(input_delivery_start_date).send_keys(delivery_start)

        self.driver.find_element_by_xpath(input_delivery_end_date).click()
        self.driver.find_element_by_xpath(input_delivery_end_date).clear()
        delivery_end = service.time_service()[5]
        self.driver.find_element_by_xpath(input_delivery_end_date).send_keys(delivery_end)

        self.driver.execute_script("window.scrollTo(0, 160);")

        wait_until_visible(self.driver, step2_button, select_type=By.XPATH)
        self.driver.find_element_by_xpath(step2_button).click()
        wait_until_visible(self.driver, step3_button, select_type=By.XPATH)
        self.driver.find_element_by_xpath(step3_button).click()

        file_to_upload = service.relative2absolute('./doc1.docx')
        sleep(1)
        self.driver.find_element_by_xpath(add_doc).click()
        sleep(2)
        wait_for_presence(self.driver, upload_document, select_type=By.XPATH)
        self.driver.find_element_by_xpath(upload_document).send_keys(file_to_upload)
        self.driver.find_element_by_xpath(select_doc_type).click()
        self.driver.find_element_by_xpath(select_doc_type_1).click()
        wait_until_visible(self.driver, upload_verif, select_type=By.XPATH)

        self.driver.find_element_by_css_selector(submit_create_tender).click()
        wait_until_visible(self.driver, close_popup_window, select_type=By.XPATH)
        self.driver.find_element_by_xpath(close_popup_window).click()


class FindTenderPage(CreateTenderPage):
    def get_tender_id(self):
        matched = False
        try:
            def find_id():
                sleep(5)
                self.driver.refresh()
                wait_until_visible(self.driver, tender_get_id_locator, select_type=By.XPATH)
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
            self.driver.quit()

        tender_id = self.driver.find_element_by_xpath(tender_get_id_locator).text
        return tender_id

    def find_tender(self, id_tender):
        tender_id = id_tender

        self.driver.get('http://dev.pzo.com.ua/tenders')
        wait_until_visible(self.driver, input_search_field, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(input_search_field).send_keys(tender_id)
        self.driver.find_element_by_css_selector(search_tender_button).click()
        sleep(5)
        wait_for_presence(self.driver, go_to_tender, select_type=By.CSS_SELECTOR)
        self.driver.find_element_by_css_selector(go_to_tender).click()
        return tender_id


class MakeBidPage:
    def __init__(self, driver):
        self.driver = driver

    def make_bid(self):

        # "LOAD_TEST_Below_Threshold"
        is_found = False
        for i in range(1, 100):
            try:
                wait_until_visible(self.driver, make_bid_button, select_type=By.XPATH)

                self.driver.find_element_by_xpath(make_bid_button).click()
                is_found = True
                break
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException):
                sleep(10)
                self.driver.refresh()

        if not is_found:
            return False

        wait_before_click(self.driver, make_bid_button, select_type=By.XPATH)
        self.driver.find_element_by_xpath(make_bid_button).click()

        self.driver.execute_script("window.scrollTo(0, 273);")
        wait_until_visible(self.driver, input_bid_amount, select_type=By.XPATH)
        self.driver.find_element_by_xpath(input_bid_amount).send_keys(3000)

        file_to_upload = service.relative2absolute('./doc1.docx')

        wait_until_visible(self.driver, add_bid_doc, select_type=By.XPATH)
        self.driver.find_element_by_xpath(add_bid_doc).click()

        wait_until_visible(self.driver, upload_document, select_type=By.XPATH)
        self.driver.find_element_by_xpath(upload_document).send_keys(file_to_upload)

        self.driver.find_element_by_xpath(select_doc_type).click()
        self.driver.find_element_by_xpath(select_doc_type_1).click()
        wait_until_visible(self.driver, upload_bid_verif, select_type=By.XPATH)

        return True

    def run_bid(self):
        sleep(3)
        self.driver.find_element_by_xpath(submit_bid_button).click()
        sleep(5)
        try:
            wait_for_text_presence(self.driver, verif_bid_success, u'Пропозиція створена', select_type=By.XPATH)
            sleep(5)
        except TimeoutException as error:
            print(error)
            raise error

        return True
