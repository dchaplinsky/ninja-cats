from flask_mongoengine import Document
from mongoengine import (
    StringField, ReferenceField, IntField, BooleanField
)

__all__ = ['MenuItem', 'get_menu']


class MenuItem(Document):
    title = StringField()
    link = StringField()
    icon_class = StringField()
    page_link = ReferenceField('StaticPage')
    guest_menu = BooleanField()
    registered_menu = BooleanField()
    order = IntField()

    meta = {
        'collection': 'cms.menuItems',
        'allow_inheritance': True,
        'indexes': ["guest_menu", "registered_menu", "order"]
    }


def get_menu():
    return {
        "guest_menu_items": MenuItem.objects.filter(
            guest_menu=True).order_by("order"),
        "registered_menu_items": MenuItem.objects.filter(
            registered_menu=True).order_by("order")
    }
