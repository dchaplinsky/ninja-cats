from flask_mongoengine import Document
from mongoengine import (
    StringField, ReferenceField
)

__all__ = ['MenuItem', 'get_menu']


class MenuItem(Document):
    title = StringField()
    link = StringField()
    icon_class = StringField()
    page_link = ReferenceField('StaticPage')

    meta = {
        'collection': 'cms.menuItems',
        'allow_inheritance': True,
        'indexes': []
    }


def get_menu():
    return {
        "menu_items": MenuItem.objects.all()
    }
