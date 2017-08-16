from vulyk.admin.models import AuthModelView, CKTextAreaField
from wtforms.validators import Required

__all__ = ['FAQAdmin']


class FAQAdmin(AuthModelView):
    form_overrides = dict(answer=CKTextAreaField)
    column_exclude_list = ['answer', ]


class StaticPageAdmin(AuthModelView):
    form_overrides = dict(body=CKTextAreaField)
    column_exclude_list = ['body', ]
    form_args = {
        'slug': {
            'validators': [Required()]
        }
    }


class PromoAdmin(AuthModelView):
    form_overrides = dict(body=CKTextAreaField)
    column_exclude_list = ['body', 'image']


class MenuAdmin(AuthModelView):
    form_choices = {
        'icon_class': [
            ('ft-home', 'ft-home'),
            ('ft-heart', 'ft-heart'),
            ('ft-info', 'ft-info'),
        ]
    }

    column_exclude_list = ['icon_class']

    form_args = {
        'title': {
            'validators': [Required()]
        }
    }
