from collections import OrderedDict
import datetime

from peewee import *

db = SqliteDatabase('diary.db')

menu = OrderedDict({
    ('a', 'add_entry'),
    ('v', 'view_entries'),  
}

)


class Entry(Model):
    content = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    # timestamp

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""


def add_entry():
    """Add an Entry."""


def view_entries():
    """View previous entries."""


def delete_entry(entry):
    """Delete an entry."""



if __name__ == '__main__':
    initialize()
    menu_loop()
