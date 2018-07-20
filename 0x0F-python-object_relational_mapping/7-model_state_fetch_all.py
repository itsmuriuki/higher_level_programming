#!/usr/bin/python3
"""
Script that lists all State objects from the database
"""

from sys import argv
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

user = argv[1]
password = argv[2]
database = argv[3]

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id.asc()).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
