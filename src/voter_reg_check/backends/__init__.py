from .voteorg import check as check_voteorg
from .rockthevote import check as check_rockthevote

checkers = {
    "rockthevote": check_rockthevote,
    "voteorg": check_voteorg
    }

def check(method, voterinfo):
    return checkers[method](**voterinfo)
