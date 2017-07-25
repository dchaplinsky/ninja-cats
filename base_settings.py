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
    "assets/scss/fonts.scss",
    "app-assets/scss/bootstrap.scss",
    "app-assets/fonts/feather/style.min.css",
    "app-assets/fonts/font-awesome/css/font-awesome.min.css",
    "app-assets/vendors/css/extensions/pace.css",
    "app-assets/scss/bootstrap-extended.scss",
    "app-assets/scss/app.scss",
    "app-assets/scss/colors.scss",
    "app-assets/scss/core/menu/menu-types/horizontal-menu.scss",
    "app-assets/scss/core/menu/menu-types/vertical-overlay-menu.scss",
    "app-assets/scss/pages/gallery.scss",
    "assets/scss/style.scss",
]

CSS_ASSETS_OUTPUT = ENV('CSS_ASSETS_OUTPUT', 'styles/packed.css')
CSS_ASSETS_FILTERS = ENV('CSS_ASSETS_FILTERS', ('scss', 'yui_css', 'cssrewrite'))
# CSS_ASSETS_FILTERS = ENV('CSS_ASSETS_FILTERS', ('cssrewrite',))
