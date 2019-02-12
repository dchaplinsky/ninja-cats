import os
import os.path

def get_env_str(k, default):
    return os.environ.get(k, default)

def get_env_str_list(k, default=""):
    if os.environ.get(k) is not None:
        return os.environ.get(k).strip().split(" ")
    return default

ENV = os.environ.get

TEMPLATES_FOLDER = os.path.join(os.path.dirname(__file__), "templates")

LOGGING_LOCATION = "/tmp/vulyk.log"
ENABLE_ADMIN = True

STATIC_FOLDER = get_env_str('STATIC_ROOT', os.path.join(os.path.dirname(__file__), "static"))

JS_ASSETS = [
    "app-assets/vendors/js/vendors.min.js",
    "app-assets/vendors/js/charts/chart.min.js",
    "app-assets/vendors/js/tables/jquery.dataTables.min.js",
    "app-assets/vendors/js/tables/datatable/dataTables.bootstrap4.min.js",
    "app-assets/vendors/js/ui/jquery.sticky.js",
    "app-assets/vendors/js/forms/validation/jqBootstrapValidation.js",
    "app-assets/vendors/js/extensions/toastr.min.js",
    "app-assets/vendors/js/extensions/sweetalert.min.js",
    "app-assets/js/core/app-menu.js",
    "app-assets/js/core/app.js",
    "app-assets/js/scripts/gallery/fsbanner.js",
    "app-assets/js/scripts/tables/datatables/datatables.js",
    "app-assets/js/scripts/forms/validation/form-validation.js",
    "app-assets/js/scripts/forms/donate-form.js",
    "assets/js/scripts.js",
    'vendor/jquery.cookie/jquery.cookie.js',
    'vendor/jquery.hotkeys/jquery.hotkeys.js',
    'vendor/jquery.magnific-popup/jquery.magnific-popup.js',
    'scripts/base.js',
    "assets/js/user-stats.js",
    "assets/js/user-events.js",
    "assets/js/task-events.js"
]


JS_ASSETS_OUTPUT = ENV('JS_ASSETS_OUTPUT', 'scripts/packed.js')
JS_ASSETS_FILTERS = ENV('JS_ASSETS_FILTERS', 'rjsmin')

CSS_ASSETS = [
    "assets/scss/_fonts.scss",
    "app-assets/scss/bootstrap.scss",
    "app-assets/fonts/simple-line-icons/style.css",
    "app-assets/fonts/font-awesome/css/font-awesome.min.css",
    "app-assets/fonts/feather/style.css",
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
    "app-assets/scss/plugins/forms/validation/form-validation.scss",
    "app-assets/scss/pages/gallery.scss",
    "app-assets/scss/pages/login-register.scss",
    "app-assets/scss/pages/fund.scss",
    "assets/scss/style.scss",


    'vendor/jquery.magnific-popup/jquery.magnific-popup.css',
    'styles/style.css'
]

CSS_ASSETS_OUTPUT = ENV('CSS_ASSETS_OUTPUT', 'styles/packed.css')
CSS_ASSETS_FILTERS = ENV('CSS_ASSETS_FILTERS', ('scss', 'cssrewrite'))

BADGE_PATH = "static/badges"

ENABLED_BLUEPRINTS = [
    {
        'path': 'vulyk.blueprints.gamification.gamification',
        'config': {
            "badges": [
                (os.path.join(BADGE_PATH, f), f)
                for f in os.listdir(BADGE_PATH) if os.path.isfile(os.path.join(BADGE_PATH, f))
            ],
            "levels": {
                1: 5,
                2: 20,
                3: 34,
                4: 40,
                5: 48,
                6: 56,
                7: 66,
                8: 77,
                9: 89,
                10: 103,
                11: 119,
                12: 138,
                13: 158,
                14: 182,
                15: 208,
                16: 238,
                17: 272,
                18: 311,
                19: 354,
                20: 403,
                21: 458,
                22: 520,
                23: 590,
                24: 669,
                25: 758,
                26: 858,
                27: 970,
                28: 1095,
                29: 1237,
                30: 1395,
                31: 1573,
                32: 1773,
                33: 1997,
                34: 2248,
                35: 2529,
                36: 2843,
                37: 3196,
                38: 3590,
                39: 4032,
                40: 4525,
                41: 5078,
                42: 5695,
                43: 6385,
                44: 7156,
                45: 8017,
                46: 8980,
                47: 10054,
                48: 11253,
                49: 12592,
                50: 14086,
                51: 15753,
                52: 17613,
                53: 19687,
                54: 21999,
                55: 24577,
                56: 27451,
                57: 30654,
                58: 34222,
                59: 38198,
                60: 42627,
                61: 47560,
                62: 53052,
                63: 59168,
                64: 65977,
                65: 73555,
                66: 81989,
                67: 91375,
                68: 101818,
                69: 113436,
                70: 126359,
                71: 140732,
                72: 156717,
                73: 174491,
                74: 194253,
                75: 216222,
                76: 240642,
                77: 267784,
                78: 297949,
                79: 331468,
                80: 368712,
                81: 410089,
                82: 456055,
                83: 507114,
                84: 563823,
                85: 626804,
                86: 696742,
                87: 774399,
                88: 860621,
                89: 956344,
                90: 1062604,
                91: 1180553,
                92: 1311466,
                93: 1456756,
                94: 1617989,
                95: 1796901,
                96: 1995416,
                97: 2215665,
                98: 2460010,
                99: 2731066,
                100: 3031734,
            }
        },
        'url_prefix': 'gamification'
    },
    {
        'path': 'blueprints.cms.cms',
        'config': {},
        'url_prefix': 'cms'
    },
]

REDIRECT_USER_AFTER_LOGIN = False
SITE_URL = "https://kotyky.org.ua"
SITE_NAME = "Котики"
SITE_FB_APP_ID = "1394419294211706"

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, age_range'
}
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

SENTRY_DSN = get_env_str('SENTRY_DSN', None)

WARM_WELCOME = u"""<h3>Вас вітає Канцелярська сотня.</h3>
<p>Сайт <a href="http://sotnya.org.ua">sotnya.org.ua</a>, це місце спільної роботи волонтерів над масштабними проектами, які складаються з невеличких зусиль кожного. Сьогодні Канцелярська сотня займається розшифровкою та переведенням у електронну форму декларацій чиновників, депутатів, правоохоронців та інших державних службовців.</p>
<p>Після входу на сайт (кнопка Фейсбук справа), система запропонує вам скачати декларацію про доходи, та внести дані з неї у спеціально розроблену форму.</p>
<p>Зробіть це будь-ласка. Ви вкладетесь у максимум 15 хвилин часу. А ваша робота дозволить нам зробити автоматичний аналіз даних.</p>
<p>Якщо у вас є більше часу - система із задоволенням надасть вам ще одну декларацію. І ще. І ще. Ми будемо щасливі, якщо ви заповните кілька десятків, адже цього року чиновники мають оприлюднити майже мільйон декларацій.</p>
<p>Результати розшифровки відкрито доступні на сайті <a href="http://declarations.com.ua">declarations.com.ua</a>.</p>"""

GA = get_env_str('GA', None)

SOCIAL_AUTH_FACEBOOK_KEY = get_env_str('SOCIAL_AUTH_FACEBOOK_KEY', None)
SOCIAL_AUTH_FACEBOOK_SECRET = get_env_str('SOCIAL_AUTH_FACEBOOK_SECRET', None)

SOCIAL_AUTH_TWITTER_KEY = get_env_str('SOCIAL_AUTH_TWITTER_KEY', None)
SOCIAL_AUTH_TWITTER_SECRET = get_env_str('SOCIAL_AUTH_TWITTER_SECRET', None)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_env_str('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', None)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_env_str('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', None)

DEBUG_TB_PANELS = [ ]

COLLECT_STATIC_ROOT = get_env_str('STATIC_ROOT', STATIC_FOLDER)
COLLECT_STORAGE = 'vulyk.ext.storage'

ENABLED_TASKS = {
    'vulyk_declaration': 'DeclarationTaskType',
    'vulyk_judges': 'JudgesTaskType'
}

MONGODB_SETTINGS = {
    'HOST': get_env_str('DB_HOST', "localhost"),
    'DB': get_env_str('DB_NAME', "ninja_cats"),
    'USERNAME': get_env_str('DB_USER', "ninja_cats"),
    'PASSWORD': get_env_str('DB_PASS', "irDJrZ7EMmiZ"),
    'PORT': int(get_env_str('DB_PASS', "27017")),
}

LOG_TO_STDERR = ENV('LOG_TO_FILE', "False").lower() in ("true", "t", "1")
