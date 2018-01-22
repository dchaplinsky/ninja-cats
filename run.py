#!/usr/bin/env python

import sys
from vulyk.app import app

if app.config.get("SENTRY_DSN"):
    from raven.contrib.flask import Sentry
    sentry = Sentry(app, dsn=app.config["SENTRY_DSN"])


if __name__ == '__main__':
    extra_files = None

    if app.debug:
        extra_files = app._base_files_to_watch + app._plugin_files_to_watch

    if len(sys.argv) > 1:
        app.run(sys.argv[1], extra_files=extra_files)
    else:
        app.run(extra_files=extra_files)
