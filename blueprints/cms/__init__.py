from vulyk.blueprints import VulykModule
from .admin import FAQAdmin, StaticPageAdmin, PromoAdmin
from .models.faq import FAQItem, get_faq_on_main
from .models.static import StaticPage
from .models.promo import PromoItem, get_promos_on_main

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


cms = CMSModule('cms', __name__)
cms.add_context_filler(get_faq_on_main)
cms.add_context_filler(get_promos_on_main)
