import logging

from connexion import NoContent

from ..backends.voteamerica import check


_logger = logging.getLogger(__name__)


def post(body):
    r = {"result": check(**body), "voter_info": body}
    return r, 200
