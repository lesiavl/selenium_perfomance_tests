from selenium.webdriver.support.ui import Select
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import os


def select_option(driver, select_locator, option):
    select_some_option = Select(driver.find_element_by_xpath(select_locator))
    return select_some_option.select_by_visible_text(option)


def relative2absolute(relative_path):
    return os.path.abspath(relative_path)


def time_service():
    enquiry_time_start = parse(str(datetime.now() + timedelta(days=1)))
    enquiry_time_start = enquiry_time_start.strftime("%Y-%m-%d %H:%M")

    enquiry_time_end = parse(str(datetime.now() + timedelta(days=2)))
    enquiry_time_end = enquiry_time_end.strftime("%Y-%m-%d %H:%M")

    tender_time_start = parse(str(datetime.now() + timedelta(days=3)))
    tender_time_start = tender_time_start.strftime("%Y-%m-%d %H:%M")

    tender_time_end = parse(str(datetime.now() + timedelta(days=4)))
    tender_time_end = tender_time_end.strftime("%Y-%m-%d %H:%M")

    t = (enquiry_time_start, enquiry_time_end, tender_time_start, tender_time_end)
    return list(t)


def scroll_to_element(driver, element):
    return driver.execute_script("return arguments[0].scrollIntoView();", element)


