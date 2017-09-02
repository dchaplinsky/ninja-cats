#!/usr/bin/env python

import sys
from vulyk.app import app

if __name__ == '__main__':
    extra_files = None

    if app.debug:
        extra_files = app._base_files_to_watch + app._plugin_files_to_watch

    if len(sys.argv) > 1:
        app.run(sys.argv[1], extra_files=extra_files)
    else:
        app.run(extra_files=extra_files)
