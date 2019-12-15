#!/usr/bin/python3
""" this class gets the content of a table """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    getstate = session.query(State).filter(State.name == sys.argv[4]).first()

    if (getstate):
        print("{}".format(getstate.id))
    else:
        print("Not Found")
    session.close()
