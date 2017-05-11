#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_objects import *
from selenium import webdriver

import datetime
import time
import Queue
import threading

import traceback


tenders = Queue.Queue()
tenders_ids = []
tenders_threads = 1

bids = Queue.Queue()
bids_failed = {}

runs = Queue.Queue()


class CreateTenders(threading.Thread):
    exited = False

    def __init__(self, queue, driver):
        threading.Thread.__init__(self)
        self.queue = queue
        self.driver = driver
        self.login_page_owner = LoginPage(
            owner_users['email'], owner_users['password'], self.driver
        )
        self.create_tender_page = CreateTenderPage(self.driver)
        self.find_tender = FindTenderPage(self.driver)

    def run(self):
        while True:
            # Wait for start
            self.queue.get()
            
            # Process business logic
            self.driver.get(broker['url'])
            try:
                self.login_page_owner.login_as_owner()
                self.driver.get(create_tender_url)
                self.create_tender_page.create_tender()

                tenders_ids.append(self.find_tender.get_tender_id())
            except Exception as error:
                self.driver.close()
                self.exited = True
                print(error)
                traceback.print_exc()
                raise error
            finally:
                if not self.exited:
                    self.driver.close()

                self.queue.task_done()


class MakeTendersBids(threading.Thread):
    exited = False

    def __init__(self, queue, user, password, tender_id, driver):
        threading.Thread.__init__(self)
        self.queue = queue
        self.driver = driver
        self.tender_id = tender_id
        self.login_page_provider = LoginPage(user, password, self.driver)
        self.find_tender = FindTenderPage(self.driver)
        self.make_bid_page = MakeBidPage(self.driver)

    def run(self):
        while True:
            # Wait for start
            self.queue.get()
            self.driver.get(broker['url'])

            # Process business logic
            try:
                self.login_page_provider.login_as_provider()
                self.find_tender.find_tender(self.tender_id)

                if not self.make_bid_page.make_bid():
                    bids_failed[self.tender_id] = 'failed'
                    print('Bid failed for tender: {}'.format(self.tender_id))
                    return
                
                bids_failed[self.tender_id] = 'passed'
                print('Bid success for tender {}'.format(self.tender_id))
            except Exception as error:
                self.driver.close()
                self.exited = False
                print(error)
                traceback.print_exc()
                raise error
            finally:
                self.queue.task_done()


class RunTenderBids(threading.Thread):
    def __init__(self, queue, driver, providerAndTender):
        threading.Thread.__init__(self)
        self.queue = queue
        self.driver = driver
        self.make_bid_page = MakeBidPage(self.driver)
        self.providerAndTender = providerAndTender

    def run(self):
        while True:
            # Wait for start
            self.queue.get()

            # Process business logic
            try:
                with open('load_results.txt', 'a') as fl:
                    fl.write('{} started bid for {} —---------------- STARTED\n'.format(self.providerAndTender, datetime.datetime.now()))
                    self.make_bid_page.run_bid()
                    fl.write('{} made bid for {} —---------------- FINISHED\n'.format(self.providerAndTender, datetime.datetime.now()))
                    fl.close()
            finally:
                self.queue.task_done()

start = time.time()

# Start creating tenders

print('Start creating tenders...')
for i in range(tenders_threads):
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 1000)
    t = CreateTenders(tenders, driver)
    t.setDaemon(True)
    t.start()

for i in range(tenders_threads):
    tenders.put(True)

# Wait for all to complete 
tenders.join()
print('Tenders created - ' + ', '.join(tenders_ids))

# Start making tenders bids
print('Start making bids...')
drivers = {}
for tid in tenders_ids:
    for provider in provider_users.items():
        driver = webdriver.Chrome()
        driver.set_window_size(1200, 1000)
        drivers['{} {}'.format(provider[0], tid)] = driver

        b = MakeTendersBids(bids, provider[0], provider[1], tid, driver)
        b.setDaemon(True)
        print(provider[0], tid)
        b.start()

for tid in tenders_ids:
    for provider in provider_users.items():
        bids.put(True)

bids.join()

print('Bids made')
print(bids_failed)

with open('load_results.txt', 'a') as f:
    f.write('{} failed \n'.format(bids_failed))
    f.close()

# Start making by clicking simultaneously
print('Start running bids...')
for driver in drivers.keys():
    c = RunTenderBids(runs, drivers[driver], driver)
    c.setDaemon(True)
    c.start()

for driver in drivers:
    runs.put(True)

runs.join()
print('Runs performed')

print("Elapsed Time: %s" % (time.time() - start))

for driver in drivers:
    drivers[driver].close()
