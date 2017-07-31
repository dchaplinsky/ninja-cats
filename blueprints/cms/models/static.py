from flask_mongoengine import Document
from mongoengine import (
    ComplexDateTimeField, StringField
)

__all__ = ['StaticPage']


class StaticPage(Document):
    title = StringField()
    body = StringField()
    slug = StringField(min_length=2)
    last_changed = ComplexDateTimeField(db_field='lastChanged')

    meta = {
        'collection': 'cms.staticPage',
        'allow_inheritance': True,
        'indexes': [
            'slug'
        ]
    }
