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
    stateLo = State(name='Louisiana')
    session.add(stateLo)
    newState = session.query(State).filter_by(name="Louisiana").first()
    print("{}".format(newState.id))
    session.commit()
    session.close()
