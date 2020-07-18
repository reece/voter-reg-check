from .voteamerica import check as check_voteamerica
from .rockthevote import check as check_rockthevote

checkers = {
    "rockthevote": check_rockthevote,
    "voteamerica": check_voteamerica
    }

def check(method, voterinfo):
    return checkers[method](**voterinfo)
