"""use Vote America to check voter registration"""

import logging

import dateutil.parser
import requests


_logger = logging.getLogger(__name__)


submit_url = "https://am-i-registered-to-vote.org/verify-registration.php"
default_email_address = "bogus@bogus.com"


def check(first_name, last_name, street_address, apartment, city, state_abbrev, zip_5, dob, email=None):
    
    _logger.info("check(...)")

    dob_dt = dateutil.parser.parse(dob)

    data = {
        "cons_email": email or default_email_address,
        "cons_info_component": "t",
        "blah": "rtv-wl-verify",
        "group_ids": "89407",
        "interest_id": "1",
        "partner_id": "1", 
        "source": "",
        "sub_source": "rtv-wl-verify",
        "wl_partner_optin": "0",
    }

    user_data = {
        "birth_date_day": dob_dt.day,
        "birth_date_month": dob_dt.month,
        "birth_date_year": dob_dt.year,
        "cons_city": city,
        "cons_first_name": first_name,
        "cons_last_name": last_name, 
        "cons_state": state_abbrev,
        "cons_street1": street_address,
        "cons_street2": "",
        "cons_zip_code": zip_5,
    }

    data.update(user_data)
    resp = requests.post(submit_url, data=data)
    resp.raise_for_status()
    return "you are registered" in resp.content.decode()


if __name__ == "__main__":
    test_results = [
        ({"first_name": "Reece", "last_name": "Hart", "dob": "11/22/1968",
          "street_address": "1 Sussex St.", "apartment": "",
          "city": "San Francisco", "state_abbrev": "CA",
          "zip_5": "94131"}, True)
        ]

    for test, exp in test_results:
        obs = check(**test)
        r = "✔" if exp == obs else "✘"
        print(f"{r} ({exp}) | {test}")

