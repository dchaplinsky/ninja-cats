import flask
from datetime import datetime
from decimal import Decimal
import flask_login as login
import gridfs
from bson.objectid import ObjectId
from mongoengine.connection import get_db

from vulyk.blueprints import VulykModule
from vulyk.utils import HTTPStatus
from vulyk.blueprints.gamification.models.foundations import FundModel
from vulyk.blueprints.gamification.models.rules import RuleModel

from vulyk.models.user import User
from vulyk.signals import on_task_done
from vulyk.blueprints.gamification.core.events import Event
from vulyk.blueprints.gamification.core.state import UserState
from vulyk.blueprints.gamification.models.events import EventModel
from vulyk.blueprints.gamification.models.state import UserStateModel

from .admin import FAQAdmin, StaticPageAdmin, PromoAdmin, MenuAdmin
from .models.faq import FAQItem, get_faq_on_main
from .models.static import StaticPage, get_task_pages
from .models.promo import PromoItem, get_promos_on_main
from .models.menu import MenuItem, get_menu
from .models.referals import Referal
from .utils import ukr_plural

__all__ = [
    'cms'
]


class CMSModule(VulykModule):
    def register(self, app, options, first_registration=False):
        super().register(app, options, first_registration)
        self.app = app

        @app.template_filter("uk_plural")
        def uk_plural(value, args):
            args = args.split(',')
            return ukr_plural(value, *args)

        if app.config.get('ENABLE_ADMIN', False):
            app.admin.add_view(FAQAdmin(FAQItem))
            app.admin.add_view(StaticPageAdmin(StaticPage))
            app.admin.add_view(PromoAdmin(PromoItem))
            app.admin.add_view(MenuAdmin(MenuItem))

        @flask.request_finished.connect_via(app)
        def track_affiliate_link(sender, response, **extra):
            if "aff" in flask.request.args:
                u = User.get_by_id(flask.request.args["aff"])

                if u is not None:
                    response.set_cookie(
                        'affiliate_id',
                        flask.request.args["aff"],
                        httponly=True,
                        max_age=60 * 60 * 24 * 30
                    )


cms = CMSModule('cms', __name__)


@cms.route('/thumbnail/<coll>/<pk>')
def api_file_view(coll, pk):
    if not pk or not coll:
        flask.abort(HTTPStatus.NOT_FOUND)

    if coll not in ["images"]:
        flask.abort(HTTPStatus.FORBIDDEN)

    fs = gridfs.GridFS(get_db("default"), coll)

    data = fs.get(ObjectId(pk))
    if not data:
        flask.abort(HTTPStatus.NOT_FOUND)

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
        flask.abort(HTTPStatus.NOT_FOUND)

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
        flask.abort(HTTPStatus.NOT_FOUND)

    return flask.render_template(
        "base/fund_page.html",
        fund=fund
    )


@cms.route('/achievement/<rule_id>')
def achievement_page(rule_id):
    try:
        rule = RuleModel.objects.get(id=rule_id).to_rule()
    except RuleModel.DoesNotExist:
        flask.abort(HTTPStatus.NOT_FOUND)

    return flask.render_template(
        "base/rule_page.html",
        rule=rule
    )


@on_task_done.connect
def track_affiliates(sender, answer):
    affiliate_id = flask.request.cookies.get('affiliate_id')
    user = flask.g.user

    if affiliate_id is not None and user.is_authenticated:
        u = User.get_by_id(affiliate_id)
        existing_referal = Referal.objects.filter(
            invitee=user).first()

        if u is not None and existing_referal is None and u.id != user.id:
            dt = datetime.utcnow()  # TODO: TZ Aware?
            state = UserStateModel.get_or_create_by_user(u)

            UserStateModel.update_state(
                diff=UserState(
                    user=u,
                    potential_coins=Decimal(),
                    level=state.level,
                    points=Decimal("1.0"),
                    actual_coins=Decimal("1.0"),
                    achievements=[],
                    last_changed=dt))

            EventModel.from_event(
                Event.build(
                    timestamp=dt,
                    user=u,
                    answer=None,
                    points_given=Decimal("1.0"),
                    coins=Decimal("1.0"),
                    achievements=[],
                    acceptor_fund=None,
                    level_given=None,
                    viewed=False)
            ).save()

            Referal.objects.create(
                inviter=u,
                invitee=user
            )


def get_foundations():
    return {
        "foundations": list(map(
            lambda f: f.to_dict(),
            FundModel.get_funds()
        ))
    }


def get_site_url():
    res = {
        "SITE_URL": cms.app.config.get('SITE_URL', False),
        "SITE_FB_APP_ID": cms.app.config.get('SITE_FB_APP_ID', False),
    }

    if flask.g.user.is_authenticated: 
        res["AFFILIATE_URL"] = (
            cms.app.config.get('SITE_URL', False) +
            "?aff={}".format(flask.g.user.id)
        )

    return res

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
cms.add_context_filler(get_site_url)
cms.add_context_filler(get_task_pages)
