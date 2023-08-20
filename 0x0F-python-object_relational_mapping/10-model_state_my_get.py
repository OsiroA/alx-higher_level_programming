#!/usr/bin/python3
'''
This script prints the State object with the name passed as an argument
from a given database
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
    Base.metadata.create_all(database_engine)
    Session = sessionmaker(bind=database_engine)

    session = Session()

    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
