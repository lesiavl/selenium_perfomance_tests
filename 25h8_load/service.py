from selenium.webdriver.support.ui import Select
from datetime import datetime
from datetime import timedelta
import os


def select_option(driver, select_locator, option):
    select_some_option = Select(driver.find_element_by_xpath(select_locator))
    return select_some_option.select_by_visible_text(option)


def time_service():
    now = datetime.now()
    enquiry_date_end = datetime.now() + timedelta(minutes=2)
    enquiry_date_end = enquiry_date_end.strftime("%d/%m/%Y %H:%M")

    tender_date_start = datetime.now() + timedelta(minutes=4)
    tender_date_start = tender_date_start.strftime("%d/%m/%Y %H:%M")

    tender_date_end = datetime.now() + timedelta(hours=3)
    tender_date_end = tender_date_end.strftime("%d/%m/%Y %H:%M")

    delivery_date_start = datetime.now() + timedelta(days=2)
    delivery_date_start = delivery_date_start.strftime("%d/%m/%Y %H:%M")

    delivery_date_end = datetime.now() + timedelta(days=4)
    delivery_date_end = delivery_date_end.strftime("%d/%m/%Y %H:%M")

    result = (enquiry_date_end, tender_date_start, tender_date_end, delivery_date_start, delivery_date_end)
    return list(result)


def relative2absolute(relative_path):
    return os.path.abspath(relative_path)
