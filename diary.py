from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()



def add_entry():
    """Add an Entry."""
    print('Enter your entry.  Press Ctrl+d when finished.')
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry?  [Yn] ').lower() != 'n':
            Entry.create(content=data)
            print('Saved successfully!')


def view_entries():
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())


def delete_entry(entry):
    """Delete an entry."""


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
]

)


if __name__ == '__main__':
    initialize()
    menu_loop()
