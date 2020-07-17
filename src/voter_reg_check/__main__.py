"""start voter-reg-check webservice

"""

import logging
import os

from pkg_resources import get_distribution, resource_filename

import coloredlogs
import connexion
from flask import Flask, redirect


_logger = logging.getLogger(__name__)
__version__ = get_distribution("voter-reg-check").version


def main():
    coloredlogs.install(level="INFO")

    cxapp = connexion.App(__name__, debug=True)
    cxapp.app.url_map.strict_slashes = False

    spec_files = []

    spec_fn = resource_filename(__name__, "openapi.yaml")
    cxapp.add_api(spec_fn,
                  validate_responses=True,
                  strict_validation=True)
    spec_files += [spec_fn]

    @cxapp.route('/')
    def ui():
        return redirect("/1/ui/")

    
    _logger.info("Also watching " + str(spec_files))
    cxapp.run(host="0.0.0.0",
              extra_files=spec_files)

if __name__ == "__main__":
    main()
