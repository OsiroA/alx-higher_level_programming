#!/usr/bin/python3
'''
This script lists all state objects from a given database
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    '''
    This script gets the states from thr database
    '''
    database_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    database_engine = create_engine(database_uri)
    Session = sessionmaker(bind=database_engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
