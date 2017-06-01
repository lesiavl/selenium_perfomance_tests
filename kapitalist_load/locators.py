#!/usr/bin/env python
# -*- coding: utf-8 -*-
owner_users = {
    'email': 'qa_test@binka.me',
    'password': 'Password1-'
    }


provider_users = {
    'provider_user@binka.me': 'Password1-',
    'provider1_user@binka.me': 'Password1-',
    'supplier11@gmail.com': 'Kapital-Ist',
    'supplier12@gmail.com': 'Kapital-Ist',
    'supplier13@gmail.com': 'Kapital-Ist'
    }

broker = {'url': 'https://prozorro.kapital-ist.kiev.ua'}

# login

login_button = '#loginLink'
username_field = '#Email'
pass_field = '#Password'
submit_login_button = 'body > div.body-wrapper > div > div > form > div:nth-child(4) > div > input'

# create tender

create_tender_url = 'https://prozorro.kapital-ist.kiev.ua/draft/belowThreshold/createTender'

input_title = '#Title'
input_description = '#Description'

input_start_enquiry = '#EnquiryPeriod_StartDate_Local'
input_end_enquiry = '#EnquiryPeriod_EndDate_Local'
input_start_tender = '#TenderPeriod_StartDate_Local'
input_end_tender = '#TenderPeriod_EndDate_Local'
# 6/1/2017 13:00 AM format

save_draft = 'body > div.body-wrapper > div > div > form > div:nth-child(6) > div > input'
add_lot = '#draftTender > fieldset:nth-child(5) > a:nth-child(5)'

input_lot_title = '#Title'
input_lot_description = '#Description'
input_value_amount = 'body > div.body-wrapper > div > div > form > div:nth-child(5) > div.form-group > div > span.k-widget.k-numerictextbox.currency.text-box.single-line > span > input.k-formatted-value.currency.text-box.single-line.k-input'
input_min_step = '#MinimalStep_Amount'

save_draft2 = 'body > div.body-wrapper > div > div > form > div.col-md-offset-3.col-md-9 > input'

add_item = '#draftTender > fieldset:nth-child(6) > a:nth-child(5)'
input_item_description = '#Description'

select_cpv = '#ListCPVTitle'
select_cpv_1item = r'#\30 3000000-1_anchor'
cpv_selected = '#SelectedCPV'

select_unit = '#UnitId_chosen > a'
select_unit1 = '#UnitId_chosen > div > ul > li:nth-child(1)'
input_quantity = '#Quantity'
input_delivery_start_date = '#DeliveryDate_StartDate_Local'
input_delivery_end_date = '#DeliveryDate_EndDate_Local'

input_dropdown_region = 'body > div.body-wrapper > div > div > form > div:nth-child(11) > div:nth-child(5) > div > span.k-widget.k-combobox.k-header.form-control.text-box.single-line > span > input'
input_postal_code = '#DeliveryAddress_PostalCode'
input_locality = '#DeliveryAddress_Locality'
input_delivery_address = '#DeliveryAddress_Street'

save_draft3 = 'body > div.body-wrapper > div > div > form > div.col-md-offset-3.col-md-9 > input'

add_doc_button = '#draftTender > fieldset:nth-child(5) > a:nth-child(7)'
doc_title = '#Description'
doc_input = '#Document'

save_draft4 = 'body > div.body-wrapper > div > div > form > div.col-md-offset-3.col-md-9 > input'
submit_create_tender = '#submitPublish'

# search for tender

tender_get_id_locator = 'body > div.body-wrapper > div > div > h3 > a'  # xpath UA-2017-05-30-000023
# go to create tender url
select_search_type = 'body > div.body-wrapper > div > div > div:nth-child(2) > a:nth-child(2)'
input_search_field = '#ProcurementNumber'
search_tender_button = '#search'
select_tender = '#tender-table > div > table > tbody > tr > td:nth-child(1) > a'

select_bids = '#tabstrip > li:nth-child(2) > a'
make_bid_button = '#bids > div > div > a'
select_lot = '#form0 > div.modal-body > div > div.lots > div.form-group > div > label > span.cr'
input_bid_amount = '//input[@class="k-formatted-value currency text-box single-line k-input"]'

input_bid_doc = '#files'

# doc - add_doc
submit_bid_button = '#form0 > div.modal-footer > input'
delete_bid_button = '#bids > div > fieldset:nth-child(1) > div > div.col-md-2 > a'


