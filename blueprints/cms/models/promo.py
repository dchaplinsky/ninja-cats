from flask_mongoengine import Document
from mongoengine import (
    ComplexDateTimeField, StringField, BooleanField, ImageField
)

__all__ = ['PromoItem', 'get_promos_on_main']


class PromoItem(Document):
    title = StringField()
    body = StringField()
    image = ImageField(thumbnail_size=(400, 300, True))
    link = StringField()
    last_changed = ComplexDateTimeField(db_field='lastChanged')

    meta = {
        'collection': 'cms.promoItems',
        'allow_inheritance': True,
        'indexes': []
    }


def get_promos_on_main():
    return {
        "promo_items": PromoItem.objects.all()
    }
