from wtforms import fields, widgets
from vulyk.admin.models import AuthModelView
from wtforms.validators import Required

__all__ = ['FAQAdmin']


class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


class FAQAdmin(AuthModelView):
    extra_js = ['//cdn.ckeditor.com/4.7.1/standard/ckeditor.js']
    form_overrides = dict(answer=CKTextAreaField)
    column_exclude_list = ['answer', ]


class StaticPageAdmin(AuthModelView):
    extra_js = ['//cdn.ckeditor.com/4.7.1/standard/ckeditor.js']
    form_overrides = dict(body=CKTextAreaField)
    column_exclude_list = ['body', ]
    form_args = {
        'slug': {
            'validators': [Required()]
        }
    }


class PromoAdmin(AuthModelView):
    extra_js = ['//cdn.ckeditor.com/4.7.1/standard/ckeditor.js']
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
