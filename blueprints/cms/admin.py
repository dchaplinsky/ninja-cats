from vulyk.admin.models import AuthModelView, CKTextAreaField
from wtforms.validators import Required


class FAQAdmin(AuthModelView):
    form_overrides = dict(answer=CKTextAreaField)
    column_exclude_list = ('answer', )
    column_editable_list = ('order',)


class StaticPageAdmin(AuthModelView):
    form_overrides = dict(body=CKTextAreaField)
    column_exclude_list = ('body', )
    form_args = {
        'slug': {
            'validators': [Required()]
        }
    }


class PromoAdmin(AuthModelView):
    form_overrides = dict(body=CKTextAreaField)
    column_exclude_list = ('body', 'image')


class MenuAdmin(AuthModelView):
    column_exclude_list = ('icon_class',)
    column_editable_list = ('order',)

    form_args = {
        'title': {
            'validators': [Required()]
        }
    }
