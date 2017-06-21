from django.contrib.auth.models import User
from django.db.models import Model
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import CharField
from django.db.models import BooleanField


class Task(Model):
    assignee = ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='assignee')
    created_by = ForeignKey(User)

    name = CharField(max_length=1000)
    completed = BooleanField(default=False)
    description = CharField(
        max_length=10000,
        blank=True,
        null=True)

    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)
