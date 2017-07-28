#!/usr/bin/env python

import sys
from vulyk.app import app

if __name__ == '__main__':
    if len(sys.argv) > 1:
        app.run(sys.argv[1])
    else:
        app.run()
