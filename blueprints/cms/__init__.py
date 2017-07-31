from vulyk.blueprints import VulykModule
from .admin import FAQAdmin
from .models.faq import FAQItem, get_faq_on_main

__all__ = [
    'cms'
]


class CMSModule(VulykModule):

    def register(self, app, options, first_registration=False):
        super().register(app, options, first_registration)

        if app.config.get('ENABLE_ADMIN', False):
            app.admin.add_view(FAQAdmin(FAQItem))


cms = CMSModule('cms', __name__)
cms.add_context_filler(get_faq_on_main)
