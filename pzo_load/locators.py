#!/usr/bin/env python
# -*- coding: utf-8 -*-
owner_users = {'email': 'slam_ua@mail.ru',
               'password': 'qwe123qwe'}


provider_users = {'nik.urgant@mail.ru': 'qwe123qwe',
                  'maks.sotnikov.62@mail.ru': 'qwe123qwe'
                  }


broker = {'url': 'http://dev.pzo.com.ua/#login'}

# login

ukr = '(//a[@data-language="1"])[1]'
# login_button = '//a[@href="#login"]'
username_field = '#loginform-email'
pass_field = '#loginform-password'
submit_login_button = '#login-form > div.form-group.actions-wrapper.m-t-30.m-b-0 > div > button'
login_verif = '#w16 > ul > li.button-wrapper.dropdown.hidden-xs.open > a'

# create tender

create_tender_url = 'http://dev.pzo.com.ua/tender/create'

input_title = '#tenderbelowthresholdform-title'
input_description = '#tenderbelowthresholdform-description'

input_start_enquiry = """
var date = window.moment();
date.add(2, 'minutes');
$('#tenderbelowthresholdform-enquiry_period_start_date').datetimepicker().data('DateTimePicker').date(date).format('DD.MM.YYYY HH:mm')
"""

input_end_enquiry = """
var date = window.moment();
date.add(4, 'minutes');
$('#tenderbelowthresholdform-enquiry_period_end_date').datetimepicker().data('DateTimePicker').date(date).format('DD.MM.YYYY HH:mm')
"""

input_start_tender = """
var date = window.moment();
date.add(6, 'minutes');
$('#tenderbelowthresholdform-tender_period_start_date').datetimepicker().data('DateTimePicker').date(date).format('DD.MM.YYYY HH:mm')
"""

input_end_tender = """
var date = window.moment();
date.add(2, 'hours');
$('#tenderbelowthresholdform-tender_period_end_date').datetimepicker().data('DateTimePicker').date(date).format('DD.MM.YYYY HH:mm')
 """

acceleration_on = '#tenderbelowthresholdform-quick_mode'
step1_button = '#collapseGeneral > div > div:nth-child(11) > div > a'

#xpath

input_lot_title = '(//input[@class="form-control js-title"])[1]'
input_lot_description = '(//textarea[@class="form-control"])[2]'
input_value_amount = '//input[@class="form-control js-value-amount js-budget"]'
input_min_step = '//input[@class="form-control js-minstep-amount"]'

input_item_description = '(//input[@class="form-control js-title"])[2]'
input_quantity = '(//input[@class="form-control"])[10]'

select_cpv = '//a[@href="#classification"]'
select_cpv_1item = '//*[@id="1_anchor"]'
confirm_cpv = '//*[@id="classification-modal"]/div/div/div[3]/div[2]/button[1]'

# xpath
click_delivery_checkbox = '(//input[@type="checkbox"])[6]'

click_dropdown_region = '(//select[@class="form-control"])[3]'
select_region = '((//select[@class="form-control"])[3])/option[2]'
input_postal_code = '(//input[@class="form-control"])[12]'
input_locality = '(//input[@class="form-control"])[13]'
input_delivery_address = '(//input[@class="form-control"])[14]'

input_delivery_start_date = '(//input[@class="form-control"])[15]'
input_delivery_end_date = '(//input[@class="form-control"])[16]'

step2_button = '(//a[@href="#collapseFeatures"])[1]'
step3_button = '(//*[@href="#collapseDocuments"])[1]'

# xpath
# filepath
add_doc = '(//a[@href="#add-documents"])[3]'
upload_document = "//input[contains(@name, 'qqfile')]"
select_doc_type = '//select[contains(@id, "document_type")]'
select_doc_type_1 = '//select[contains(@id, "document_type")]/option[2]'
upload_verif = '(//div[@class="btn btn-default btn-custom waves-effect waves-light item js-item"])[2]'

submit_create_tender = '#submitBtn'
close_popup_window = '//button[@class="btn btn-default waves-effect waves-light btn-lg"]'

# search for
tender_get_id_locator = '#w0 > p.tender-id > span.value'

# go to create tender url
input_search_field = '#tendersearchform-query'
search_tender_button = '#tender-search-form > div > div.col-sm-5.col-md-3 > button'
go_to_tender = '#tender-list > table > tbody > tr'

# make bids
make_bid_button = '//a[@class="list-group-item"]'
input_bid_amount = '//input[@class="form-control js-amount-input"]'

add_bid_doc = '//a[@class="js-dynamic-form-add"]'
upload_bid_verif = '//div[@class="btn btn-default btn-custom waves-effect waves-light item js-item"]'

# doc - add_doc
submit_bid_button = '(//button[@type="submit"])[1]'
verif_bid_success = '//div[@class="message"]'


