from wtforms import fields, widgets
from vulyk.admin.models import AuthModelView

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
