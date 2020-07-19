#!/usr/bin/env python

import asyncio
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


async def test1vi(voter_info, mod):
    test_vi = copy.copy(voter_info)
    test_vi.update(mod)
    return [mod] + await asyncio.gather(*[check(m, test_vi) for m in methods])

async def build_results():
    results = await asyncio.gather(*[test1vi(voter_info, mod) for mod in mods])
    return results




results = asyncio.run(build_results())

print(tabulate.tabulate(results,
                        headers=["mod"] + methods))
