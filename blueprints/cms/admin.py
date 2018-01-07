from vulyk.admin.models import AuthModelView, CKTextAreaField
from wtforms.validators import Required
from wtforms.fields import SelectField


class PluginsSelectField(SelectField):
    def __init__(self, *args, **kwargs):
        choices = [
            ("", ""),
        ]

        from vulyk.app import TASKS_TYPES
        for t, v in TASKS_TYPES.items():
            choices.append((t, v.name))

        kwargs["choices"] = choices
        super(PluginsSelectField, self).__init__(*args, **kwargs)


class FAQAdmin(AuthModelView):
    form_overrides = dict(answer=CKTextAreaField)
    column_exclude_list = ('answer', )
    column_editable_list = ('order',)


class StaticPageAdmin(AuthModelView):
    form_overrides = {
        "body": CKTextAreaField,
        "task_type": PluginsSelectField,
    }
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
