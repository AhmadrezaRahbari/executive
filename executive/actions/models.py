from __future__ import unicode_literals
from builtins import object
import peewee as orm

db = orm.SqliteDatabase('executive.db')

class BaseModel(orm.Model):
    class Meta(object):
        database = db

class Project(BaseModel):
    name = orm.CharField()
    parent = orm.ForeignKeyField('self', null=True, backref='children')

class Action(BaseModel):
    name = orm.CharField()
    deadline = orm.DateField()
    project = orm.ForeignKeyField(Project, null=True)
    completed = orm.BooleanField(default = False)
    context = orm.CharField(null = True)

class ScheduledAction(BaseModel):
    """Scheduled action have a period within which they are active."""
    name = orm.CharField()
    cron = orm.CharField()
    lastcompleted = orm.DateTimeField(null = True)

db.connect()
db.create_tables([Project, Action, ScheduledAction])
