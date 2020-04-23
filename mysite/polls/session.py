import os
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Setup sqlalchemy bindings
sqlite_path = os.path.join(BASE_DIR, 'db.sqlite3')
sqlite_path_str = f"sqlite:///{sqlite_path}"
engine = sqlalchemy.create_engine(sqlite_path_str)

# Automatically read the database tables and create metadata
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)
insp = reflection.Inspector.from_engine(engine)

# Create a session, to query the tables
Session = sessionmaker(bind=engine)
session = Session()


# Create table reflection
auth_user_table = metadata.tables['auth_user']


def get_all_meta_tables() -> List:
    return insp.get_table_names()


def print_meta_columns(table):
    print(table._columns)


# Snippets
print_meta_columns(auth_user_table)
# print(get_all_meta_tables())













