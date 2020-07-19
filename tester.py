#!/usr/bin/env python
"""Compare voter registration check backends using valid and invalid
data to assess sensitivity to inaccuracies.

Currently prints something like this:

mod                                 rockthevote    voteamerica    voteorg
----------------------------------  -------------  -------------  ---------
{}                                  True           True           True
{'first_name': 'Bob'}               True           False          False
{'last_name': 'Smith'}              True           False          False
{'dob': '11/22/1967'}               True           False          True
{'street_address': '1 Surrey St.'}  True           False          False
{'city': 'San Diego'}               True           True           True
{'state_abbrev': 'CO'}              False          False          True
{'zip_5': '94122'}                  True           False          True

"""


import copy
import itertools
import logging

import tabulate

from voter_reg_check.backends import check


logging.basicConfig(level="INFO")


methods = ["rockthevote", "voteamerica", "voteorg"]
voter_info = {
    "apartment": None,
    "city": "san francisco",
    "dob": "11/22/1968",
    "first_name": "Reece",
    "last_name": "Hart",
    "state_abbrev": "CA",
    "street_address": "1 Sussex St.",
    "zip_5": "94131",
}
mods = [
    {},
    {"first_name": "Bob"},
    {"last_name": "Smith"},
    {"dob": "11/22/1967"},
    {"street_address": "1 Surrey St."},
    {"city": "San Diego"},
    {"state_abbrev": "CO"},
    {"zip_5": "94122"},
]


def test1vi(voter_info, mod):
    test_vi = copy.copy(voter_info)
    test_vi.update(mod)
    return [mod] + [check(m, test_vi) for m in methods]

def build_results():
    results = [test1vi(voter_info, mod) for mod in mods]
    return results


results = build_results()
print(tabulate.tabulate(results, headers=["mod"] + methods))
