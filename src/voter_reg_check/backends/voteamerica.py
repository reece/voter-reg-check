"""use Vote America to check voter registration"""

import logging

import bs4
import dateutil.parser
import requests

from ._lut import abbrev_us_state


_logger = logging.getLogger(__name__)


url = "https://verify.vote.org"

def check(first_name, last_name, street_address, apartment, city, state_abbrev, zip_5, dob, email=None):
    
    _logger.info("check(...)")

    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    form = soup.find("form")
    inputs = form.findAll("input")
    submit_url = url + form.get("action")
    data = {attrs["name"]: attrs.get("value", None) for attrs in (i.attrs for i in inputs)}

    dob_dt = dateutil.parser.parse(dob)

    if email is None:
        email = "bogus@bogus.com"

    user_data = {
        "apartment": apartment,
        "city": city,
        "date_of_birth_day": dob_dt.day,
        "date_of_birth_month": dob_dt.month,
        "date_of_birth_year": dob_dt.year,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "state": abbrev_us_state[state_abbrev],
        "street_address": street_address,
        "zip_5": zip_5,
        }

    data.update(user_data)
    resp = requests.post(submit_url, data=data)
    resp.raise_for_status()
    return "is registered" in resp.content.decode()


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
