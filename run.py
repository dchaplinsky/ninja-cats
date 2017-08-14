#!/usr/bin/env python

import sys
from vulyk.app import app

if __name__ == '__main__':
    # if app.debug:
    #     from flask_debugtoolbar import DebugToolbarExtension
    #     toolbar = DebugToolbarExtension(app)

    if len(sys.argv) > 1:
        app.run(sys.argv[1])
    else:
        app.run()
