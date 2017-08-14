import flask

import gridfs
from bson.objectid import ObjectId
from mongoengine.connection import get_db

from vulyk import app
from vulyk.blueprints import VulykModule

from .admin import FAQAdmin, StaticPageAdmin, PromoAdmin, MenuAdmin
from .models.faq import FAQItem, get_faq_on_main
from .models.static import StaticPage
from .models.promo import PromoItem, get_promos_on_main
from .models.menu import MenuItem, get_menu


__all__ = [
    'cms'
]


class CMSModule(VulykModule):
    def register(self, app, options, first_registration=False):
        super().register(app, options, first_registration)

        if app.config.get('ENABLE_ADMIN', False):
            app.admin.add_view(FAQAdmin(FAQItem))
            app.admin.add_view(StaticPageAdmin(StaticPage))
            app.admin.add_view(PromoAdmin(PromoItem))
            app.admin.add_view(MenuAdmin(MenuItem))


cms = CMSModule('cms', __name__)


@cms.route('/thumbnail/<coll>/<pk>')
def api_file_view(coll, pk):
    if not pk or not coll:
        flask.abort(404)

    fs = gridfs.GridFS(get_db("default"), coll)

    data = fs.get(ObjectId(pk))
    if not data:
        flask.abort(404)

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
        flask.abort(404)

    return flask.render_template(
        "base/static_page.html",
        page=page
    )


cms.add_context_filler(get_faq_on_main)
cms.add_context_filler(get_promos_on_main)
cms.add_context_filler(get_menu)
