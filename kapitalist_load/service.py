from datetime import datetime
from datetime import timedelta
import os


def time_service():
    now = datetime.now()

    enquiry_date_start = datetime.now() + timedelta(minutes=2)
    enquiry_date_start = enquiry_date_start.strftime("%m/%d/%Y %I:%M %p")

    enquiry_date_end = datetime.now() + timedelta(minutes=4)
    enquiry_date_end = enquiry_date_end.strftime("%m/%d/%Y %I:%M %p")

    tender_date_start = datetime.now() + timedelta(minutes=5)
    tender_date_start = tender_date_start.strftime("%m/%d/%Y %I:%M %p")

    tender_date_end = datetime.now() + timedelta(hours=3)
    tender_date_end = tender_date_end.strftime("%m/%d/%Y %I:%M %p")

    delivery_date_start = datetime.now() + timedelta(days=2)
    delivery_date_start = delivery_date_start.strftime("%m/%d/%Y %I:%M %p")

    delivery_date_end = datetime.now() + timedelta(days=4)
    delivery_date_end = delivery_date_end.strftime("%m/%d/%Y %I:%M %p")

    result = (enquiry_date_start, enquiry_date_end, tender_date_start, tender_date_end, delivery_date_start, delivery_date_end)
    return list(result)


def relative2absolute(relative_path):
    return os.path.abspath(relative_path)
