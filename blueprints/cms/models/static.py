from flask_mongoengine import Document
from mongoengine import (
    ComplexDateTimeField, StringField
)

__all__ = ['StaticPage', 'get_task_pages']


class StaticPage(Document):
    title = StringField()
    body = StringField()
    slug = StringField(min_length=2)
    last_changed = ComplexDateTimeField(db_field='lastChanged')
    task_type = StringField(
        max_length=50,
        null=True,
        db_field='taskType'
    )

    meta = {
        'collection': 'cms.staticPage',
        'allow_inheritance': True,
        'indexes': [
            'slug'
        ]
    }

    def __str__(self):
        return "{} ({})".format(self.title, self.slug)


def get_task_pages():
    return {
        "task_pages": {
            t.task_type: t
            for t in StaticPage.objects.filter(task_type__ne="")
        }
    }
