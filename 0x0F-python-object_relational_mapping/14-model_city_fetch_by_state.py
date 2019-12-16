#!/usr/bin/python3
""" this class gets the content of a table """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    Newtable = session.query(City, State).join(State).all()
    for city, state in Newtable:
        print('{}: ({}) {}'.format(state.name,
                                   city.id,
                                   city.name))
    session.close()
