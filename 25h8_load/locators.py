#!/usr/bin/env python
# -*- coding: utf-8 -*-
owner_users = {'email': 'prozorroytenderowner@gmail.com',
               'password': '123456'}

provider_users = {
                  'prozorroyprovider2@gmail.com': '123456'
                  }

#  'prozorroyprovider1@gmail.com': '123456',
broker = {'url': 'http://25h8.byustudio.in.ua/'}

# login

login_button = '#nav-w2 > li:nth-child(5) > a'
username_field = '#loginform-username'
pass_field = '#loginform-password'
submit_login_button = '#login-form > button'
close_notification = '#events > div > div > div.modal-header > button > i'

# create tender

create_tender_url = 'http://25h8.byustudio.in.ua/tenders/index'
create_tender_button = 'body > div > div.container > div.tenders-index.m_viewlist-wrap > div.shadow_fix > a'
input_value_amount = '#value-amount'
input_min_step = '#minimalstepvalue-amount'
input_title = '#tender-title'
input_description = '#tender-description'

# xpath
add_doc = '//*[@name="FileUpload[file]"]'
# filepath

input_item_description = '#item-0-description'
input_quantity = '#item-0-quantity'

select_cpv = '#classification-0-description'
select_cpv_1item = '//*[@id="03000000-1"]/div[1]'  # xpath
confirm_cpv = '#btn-ok'

click_dropdown_country = '//*[@id="deliveryaddress-0-countryname"]'
click_dropdown_region = '//*[@id="deliveryaddress-0-region"]'

input_locality = '#deliveryaddress-0-locality'
input_delivery_address = '#deliveryaddress-0-streetaddress'
input_postal_code = '#deliveryaddress-0-postalcode'

input_delivery_start_date = '#itemdeliverydate-0-startdate'
input_delivery_end_date = '#itemdeliverydate-0-enddate'

input_end_enquiry = '#enquiryperiod-enddate'

input_start_tender = '#period-startdate'
input_end_tender = '#period-enddate'

input_procuring_entity = '#tender_simple_create > div.info-block.m_info > div > div.info-block.contact_block > div.form-group.is-empty > div > select > option:nth-child(2)'
submit_create_tender = 'body > div > div.container > div.col-md-offset-3.col-md-9 > button.btn.btn-default.btn_submit_form'

# search for tender

tender_get_id_locator = '//span[@tid="tenderID"]'  # xpath
# go to create tender url
input_search_field = '#tenderssearch-tender_cbd_id'
search_tender_button = '#w0 > div:nth-child(4) > div:nth-child(2) > button'
select_tender = '#w1 > div:nth-child(2) > div.panel.panel-default > div > div.col-md-3 > div > a'

# make_bid_button =
input_bid_amount = '#value-amount'

# doc - add_doc
submit_bid_button = '#submit_bid'
delete_bid_button = '#bid_form > div.row.submit-buttons > button.btn.btn-danger'


