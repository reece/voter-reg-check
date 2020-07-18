from .rockthevote import check as check_rockthevote
from .voteamerica import check as check_voteamerica
from .voteorg import check as check_voteorg

checkers = {
    "rockthevote": check_rockthevote,
    "voteamerica": check_voteamerica,
    "voteorg": check_voteorg,
    }

def check(method, voterinfo):
    return checkers[method](**voterinfo)
