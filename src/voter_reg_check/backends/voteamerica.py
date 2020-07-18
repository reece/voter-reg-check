"""use Vote America to check voter registration"""

import logging
import uuid

import dateutil.parser
import requests


_logger = logging.getLogger(__name__)


submit_url = "https://api.voteamerica.com/v1/verification/verify/?subscriber=voteamerica"
default_email_address = "bogus@bogus.com"


def check(first_name, last_name, street_address, apartment, city, state_abbrev, zip_5, dob, email=None):
    
    dob_dt = dateutil.parser.parse(dob)

    data = {
        "email": default_email_address,
        "phone": "",
        "session_id": "b4ae7ce8-d580-4f12-a4d2-5988d13de635",
        "sms_opt_in_subscriber": False,
        "embed_url": "https://www.voteamerica.com/am-i-registered-to-vote/",
    }

    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "address1": street_address,
        "city": city,
        "state": state_abbrev,
        "zipcode": zip_5,
        "date_of_birth": dob_dt.strftime("%F")
    }

    data.update(user_data)
    _logger.info(f"checking {user_data}")
    resp = requests.post(submit_url, data=data)
    resp.raise_for_status()
    return resp.json()["registered"]





