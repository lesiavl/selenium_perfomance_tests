#!/usr/bin/env python
# -*- coding: utf-8 -*-
owner_users = {'email': 'qa845@meta.ua',
               'password': 'selenide'}

provider_users = {'lexins@bigmir.net': 'fondriest'
                # 'qatest55@meta.ua': 'selenide',
                # 'test-supply@meta.ua': '0564305488',
                # 'Rudakov.d@meta.ua': '0564305488'
                  }

broker = {'url': 'https://e-test.aps-market.com/tender'}

# login

login_button = '//*[@id="login_ribbon"]/a'
username_field = '//*[@id="LoginBox"]'
pass_field = '//*[@id="LoginPasswordBox"]'
submit_login_button = '//*[@id="ButtonLogin"]'

# create tender

create_tender_button = '//*[@id="ButtonTenderAdd"]/a'
below_threshold_button = '//*[@id="menuContainer"]/li[1]/a'
input_title = '//*[@id="edtTenderTitle"]'
input_description = '//*[@id="edtTenderDetail"]'

input_value_amount = '//*[@id="edtTenderBudget"]'
input_min_step = '//*[@id="edtMinStep"]'

input_start_enquiry = """ var date = new Date();
                     date.setHours(date.getHours(), date.getMinutes() + 3);
                    $("#date_enquiry_start").datetimepicker({ allowTimes: [], format: "d.m.Y H:i", value: date })"""

input_end_enquiry = """ var date = new Date();
                   date.setHours(date.getHours(), date.getMinutes() + 5);
                    $("#date_enquiry_end").datetimepicker({ allowTimes: [], format: "d.m.Y H:i", value: date })"""

input_start_tender = """ var date = new Date();
                   date.setHours(date.getHours(), date.getMinutes() + 7);
                    $("#date_tender_start").datetimepicker({ allowTimes: [], format: "d.m.Y H:i", value: date })"""

input_end_tender = """ var date = new Date();
                    date.setDate(date.getDate() + 5);
                    $("#date_tender_end").datetimepicker({ allowTimes: [], format: "d.m.Y H:i", value: date })"""

next_button = '//*[@id="CreateTender"]'
add_item = '//*[@id="AddPoss"]'

input_item_description = '//*[@id="itemDescription"]'
input_quantity = '//*[@id="editItemQuantity"]'
select_unit = '//*[@id="window_itemadd"]/div[2]/div/div[2]/div[2]/div/div[2]/div/button/span[1]'
input_unit = '//*[@id="input_MeasureItem"]'
select_unit_1 = '//*[@id="window_itemadd"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[1]/a'

click_cpv_button = '//*[@id="button_add_cpv"]'
select_cpv_1item = '//*[@id="03000000-1_anchor"]'
confirm_cpv = '//*[@id="populate_cpv"]'

select_dkpp = '//*[@id="button_add_dkpp"]'
select_dkpp_1item = '//*[@id="000_NONE_anchor"]'
confirm_dkpp = '//*[@id="populate_dkpp"]'

input_delivery_start = """ var date = new Date();
                    date.setDate(date.getDate() + 10);
                    $("#date_delivery_start").datetimepicker({ allowTimes: [], format: "d.m.Y H:i", value: date })"""

input_delivery_end = """ var date = new Date();
                    date.setDate(date.getDate() + 13);
                    $("#date_delivery_end").datetimepicker({ allowTimes: [], format: "d.m.Y H:i", value: date })"""

delivery_checkbox = '//*[@id="shiping"]/label'
click_dropdown_country = '//*[@id="div_combo_selectCountry"]/div/button'
input_country = '//*[@id="input_CountryItem"]'
select_country = '//*[@id="div_combo_selectCountry"]/div/div/ul/li[230]/a/span[1]'

click_dropdown_region = '//*[@id="HideShow_div"]/div[1]/div/div[2]/div/div/button'
input_region = '//*[@id="input_RegionsItem"]'
select_region = '//*[@id="HideShow_div"]/div[1]/div/div[2]/div/div/div/ul/li[1]/a'

input_postal_code = '//*[@id="post_code"]'
input_locality = '//*[@id="addr_locality"]'
input_delivery_address = '//*[@id="addr_street"]'
input_latitude = '//*[@id="latitude"]'
input_longitude = '//*[@id="longitude"]'
input_height = '//*[@id="elevation"]'
save_changes = '//*[@id="AddItemButton"]'

add_tender_doc = '//*[@id="addFile"]'
select_type = '//*[@id="TypesFilesDropDown"]'
select_doc_type = '//*[@id="TypesFilesDropDown"]/option[5]'
file_input = '//*[@id="FileUpload"]'
submit_tender_doc_upload = '//*[@id="UploadFile"]'
delete_doc = '//*[@id="DelFileBtn_"]'
create_tender_draft = '//*[@id="sumbit"]'
submit_create_tender = '//*[@id="TenderPublishTop"]'

decline_electr_signature = '//*[@id="PublishConfirm"]/div[2]/div/div[2]/div[1]/div[2]/div[2]/label'
submit_popup = '//*[@id="PublishConfirm"]/div[2]/div/div[3]/button[1]'
# search for tender

tender_get_id_locator = '//*[@id="titleTenderUcode"]'

all_tenders = '//*[@id="selectjournal_name"]'
select_all_tenders = '//*[@id="selectTypeJournal"]/li[1]/a'

input_search_field = '//*[@id="search_text"]'
search_tender_button = '//*[@id="search_btn"]'
select_tender = '//p[contains(text(), "[ТЕСТУВАННЯ] LOAD_TEST_Below_Threshold")]'

# # make bid

all_bids = u'//a[contains(text(), "Пропозиції")]'
input_bid_amount = '//*[@id="editBid"]'
input_bid_doc = '//*[@id="FileUpload_bids"]'
submit_bid_doc = '//*[@id="UploadFileToBid"]'
submit_bid_button = '//*[@id="AddNoLotBid"]'

delete_bid_button = '(//*[@class="btn btn-yellow dt_button"])[2]'

