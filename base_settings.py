import os
import os.path

ENV = os.environ.get

ENABLED_TASKS = {
    'vulyk_declaration': 'DeclarationTaskType',
}

TEMPLATES_FOLDER = os.path.join(os.path.dirname(__file__), "templates")

LOGGING_LOCATION = "/tmp/vulyk.log"

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), "static")

JS_ASSETS = [
    "app-assets/vendors/js/vendors.min.js",
    "app-assets/vendors/js/ui/jquery.sticky.js",
    "app-assets/js/core/app-menu.js",
    "app-assets/js/core/app.js",
    "app-assets/js/scripts/gallery/fsbanner.js",
    "assets/js/scripts.js",
]

JS_ASSETS_OUTPUT = ENV('JS_ASSETS_OUTPUT', 'scripts/packed.js')
JS_ASSETS_FILTERS = ENV('JS_ASSETS_FILTERS', 'yui_js')

CSS_ASSETS = [
    "app-assets/css/bootstrap.css",
    "app-assets/fonts/feather/style.min.css",
    "app-assets/fonts/font-awesome/css/font-awesome.min.css",
    "app-assets/vendors/css/extensions/pace.css",
    "app-assets/css/bootstrap-extended.css",
    "app-assets/css/app.css",
    "app-assets/css/colors.css",
    "app-assets/css/core/menu/menu-types/horizontal-menu.css",
    "app-assets/css/core/menu/menu-types/vertical-overlay-menu.css",
    "app-assets/css/pages/gallery.css",
    "assets/css/style.css",
]

CSS_ASSETS_OUTPUT = ENV('CSS_ASSETS_OUTPUT', 'styles/packed.css')
CSS_ASSETS_FILTERS = ENV('CSS_ASSETS_FILTERS', ('yui_css', 'cssrewrite'))
