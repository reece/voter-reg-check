import datetime
import logging

from connexion import NoContent
import pytz

from ..backends import check


_logger = logging.getLogger(__name__)


def post(body):
    method = body["method"]
    voter_info = body["voter_info"]
    result = check(method, voter_info)
    resp = {
        "timestamp": datetime.datetime.now(tz=pytz.UTC),
        "method": method,
        "result": result,
        "voter_info": voter_info
    }
    return resp, 200
