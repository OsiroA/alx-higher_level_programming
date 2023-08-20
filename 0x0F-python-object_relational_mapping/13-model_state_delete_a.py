#!/usr/bin/python3
'''
This script changes the name of the state object
where id=2 to New Mexico to a given database
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
            argv[1], argv[2], argv[3], pool_pre_ping=True)
    database_engine = create_engine(database_uri)

    Session = sessionmaker(bind=database_engine)

    session = Session()
    # state = session.query(State).filter_by(id=2).first()
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    session.commit()
    # print(newObject.id)
    session.close()
