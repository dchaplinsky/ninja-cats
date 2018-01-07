import flask

import gridfs
from bson.objectid import ObjectId
from mongoengine.connection import get_db
from vulyk.blueprints import VulykModule
from vulyk import utils
from vulyk.blueprints.gamification.models.foundations import FundModel

from .admin import FAQAdmin, StaticPageAdmin, PromoAdmin, MenuAdmin
from .models.faq import FAQItem, get_faq_on_main
from .models.static import StaticPage, get_task_pages
from .models.promo import PromoItem, get_promos_on_main
from .models.menu import MenuItem, get_menu
from .utils import ukr_plural

__all__ = [
    'cms'
]


class CMSModule(VulykModule):
    def register(self, app, options, first_registration=False):
        super().register(app, options, first_registration)

        @app.template_filter("uk_plural")
        def uk_plural(value, args):
            args = args.split(',')
            return ukr_plural(value, *args)

        if app.config.get('ENABLE_ADMIN', False):
            app.admin.add_view(FAQAdmin(FAQItem))
            app.admin.add_view(StaticPageAdmin(StaticPage))
            app.admin.add_view(PromoAdmin(PromoItem))
            app.admin.add_view(MenuAdmin(MenuItem))


cms = CMSModule('cms', __name__)


@cms.route('/thumbnail/<coll>/<pk>')
def api_file_view(coll, pk):
    if not pk or not coll:
        flask.abort(utils.HTTPStatus.NOT_FOUND)

    if coll not in ["images"]:
        flask.abort(utils.HTTPStatus.FORBIDDEN)

    fs = gridfs.GridFS(get_db("default"), coll)

    data = fs.get(ObjectId(pk))
    if not data:
        flask.abort(utils.HTTPStatus.NOT_FOUND)

    return flask.Response(
        data.read(),
        content_type=data.content_type or "image/jpeg",
        headers={'Content-Length': data.length}
    )


@cms.route('/page/<slug>')
def static_page(slug):
    try:
        page = StaticPage.objects.get(slug=slug)
    except StaticPage.DoesNotExist:
        flask.abort(utils.HTTPStatus.NOT_FOUND)

    return flask.render_template(
        "base/static_page.html",
        page=page
    )


@cms.route('/faq')
def faq_page():
    return flask.render_template(
        "base/faq_page.html",
        faq_items=FAQItem.objects.all().order_by("order")
    )


@cms.route('/foundation/<fund_id>')
def fund_page(fund_id):
    fund = FundModel.find_by_id(fund_id)

    if fund is None:
        flask.abort(utils.HTTPStatus.NOT_FOUND)

    return flask.render_template(
        "base/fund_page.html",
        fund=fund
    )


def get_foundations():
    return {
        "foundations": list(map(
            lambda f: f.to_dict(),
            FundModel.get_funds()
        ))
    }


def get_tasks():
    from vulyk.app import TASKS_TYPES
    user = flask.g.user

    if user.is_authenticated:
        return {
            "task_types": [
                x.to_dict() for x in TASKS_TYPES.values()
                if user.is_eligible_for(x.type_name)
            ]
        }
    else:
        return {}


cms.add_context_filler(get_faq_on_main)
cms.add_context_filler(get_promos_on_main)
cms.add_context_filler(get_menu)
cms.add_context_filler(get_foundations)
cms.add_context_filler(get_tasks)
cms.add_context_filler(get_task_pages)
