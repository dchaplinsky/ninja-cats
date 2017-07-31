import os
import os.path

ENV = os.environ.get

ENABLED_TASKS = {
    'vulyk_declaration': 'DeclarationTaskType',
}

TEMPLATES_FOLDER = os.path.join(os.path.dirname(__file__), "templates")

LOGGING_LOCATION = "/tmp/vulyk.log"
ENABLE_ADMIN = True

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), "static")

JS_ASSETS = [
    "app-assets/vendors/js/vendors.min.js",
    "app-assets/vendors/js/charts/chart.min.js",
    "app-assets/vendors/js/extensions/jquery.knob.min.js",
    "app-assets/vendors/js/tables/jquery.dataTables.min.js",
    "app-assets/vendors/js/tables/datatable/dataTables.bootstrap4.min.js",
    "app-assets/vendors/js/ui/jquery.sticky.js",
    "app-assets/js/core/app-menu.js",
    "app-assets/js/core/app.js",
    "app-assets/js/scripts/gallery/fsbanner.js",
    "app-assets/js/scripts/tables/datatables/datatables.js",
    "assets/js/scripts.js",
    "assets/js/user-stats.js",
]


JS_ASSETS_OUTPUT = ENV('JS_ASSETS_OUTPUT', 'scripts/packed.js')
JS_ASSETS_FILTERS = ENV('JS_ASSETS_FILTERS', 'rjsmin')

CSS_ASSETS = [
    "assets/scss/_fonts.scss",
    "app-assets/scss/bootstrap.scss",
    "app-assets/fonts/feather/style.min.css",
    "app-assets/fonts/font-awesome/css/font-awesome.min.css",
    "app-assets/fonts/simple-line-icons/style.css",
    "app-assets/vendors/css/extensions/pace.css",
    "app-assets/vendors/css/forms/icheck/icheck.css",
    "app-assets/vendors/css/forms/icheck/custom.css",
    "app-assets/vendors/css/extensions/sweetalert.css",
    "app-assets/vendors/css/extensions/toastr.css",
    "app-assets/vendors/css/tables/datatable/dataTables.bootstrap4.min.css",
    "app-assets/scss/bootstrap-extended.scss",
    "app-assets/scss/app.scss",
    "app-assets/scss/colors.scss",
    "app-assets/scss/core/menu/menu-types/vertical-menu.scss",
    "app-assets/scss/core/menu/menu-types/vertical-overlay-menu.scss",
    "app-assets/scss/core/menu/menu-types/horizontal-menu.scss",
    "app-assets/scss/core/menu/menu-types/vertical-overlay-menu.scss",
    "app-assets/scss/pages/gallery.scss",
    "app-assets/scss/pages/login-register.scss",
    "app-assets/scss/pages/users.scss",
    "assets/scss/style.scss",
]

CSS_ASSETS_OUTPUT = ENV('CSS_ASSETS_OUTPUT', 'styles/packed.css')
CSS_ASSETS_FILTERS = ENV('CSS_ASSETS_FILTERS', ('scss', 'cssmin', 'cssrewrite'))


ENABLED_BLUEPRINTS = [
    {
        'path': 'vulyk.blueprints.gamification.gamification',
        'config': {},
        'url_prefix': 'gamification'
    },
    {
        'path': 'blueprints.cms.cms',
        'config': {},
        'url_prefix': 'cms'
    },
]
