from flask_mongoengine import Document
from mongoengine import (
    ComplexDateTimeField, StringField, BooleanField
)

__all__ = ['FAQItem']


class FAQItem(Document):
    question = StringField()
    answer = StringField()
    last_changed = ComplexDateTimeField(db_field='lastChanged')
    on_main = BooleanField(db_field='onMain', default=True)

    meta = {
        'collection': 'cms.faqItems',
        'allow_inheritance': True,
        'indexes': [
            'on_main'
        ]
    }


def get_faq_on_main():
    return {
        "main_faq_items": FAQItem.objects.filter(on_main=True)
    }
