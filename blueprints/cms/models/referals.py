import datetime
from mongoengine import BooleanField, DateTimeField, ReferenceField
from flask_mongoengine import Document

from vulyk.models.user import User

class Referal(Document):
    """
    Main model for member entity.
    """
    inviter = ReferenceField(document_type=User, required=True)
    invitee = ReferenceField(document_type=User, required=True)
    registered = DateTimeField(default=datetime.datetime.now)

    meta = {
        'collection': 'cms.referal',
        'indexes': [
            'invitee'
        ]
    }
