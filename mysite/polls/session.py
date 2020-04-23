import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Setup sqlalchemy bindings
sqlite_path = os.path.join(BASE_DIR, 'db.sqlite3')
sqlite_path_str = f"sqlite:///{sqlite_path}"
engine = sqlalchemy.create_engine(sqlite_path_str)


# Create a session for SQLAlchemy's ORM and querying the tables
Session = sessionmaker(bind=engine)
session = Session()

# Automatically read the database tables and create metadata
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)
insp = reflection.Inspector.from_engine(engine)


# Create table reflection
auth_user_table = metadata.tables['auth_user']
polls_choice_table = metadata.tables['polls_choice']
polls_question_table = metadata.tables['polls_question']


def get_all_tables() -> List:
    """
    `get_all_tables` helper function to get a list of all tables in the database

    :return list all table names:
    """
    return insp.get_table_names()


def print_table_meta_columns(table) -> None:
    """
    `print_table_meta_columns helper function to stdout to terminal the column names of a table

    :param table:
    :return None:
    """

    print(table._columns)


# Code Snippets
django_tables = get_all_tables()
print(django_tables)

print_table_meta_columns(auth_user_table)













