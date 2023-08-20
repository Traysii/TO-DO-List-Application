from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Text, DateTime, select, insert, update, delete, or_, and_
from icecream import ic

connection_string = "sqlite:///db.sqlite3"
engine = create_engine(connection_string, echo= True)

Base = declarative_base()

class Tasks(Base):
    __tablename__ = 'todo_todo'
    
    id = Column(Integer, primary_key= True)    
    title = Column(String)
    description = Column(Text)
    complete = Column(Integer)
    timestamp = Column(DateTime)
    user_id = Column(Integer)

Session = sessionmaker(bind=engine)
session = Session()


def show_all():
    result = session.query(Tasks).all()
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def greater_than():
    result = session.query(Tasks).filter(Tasks.id > 5)
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def less_than():
    result = session.query(Tasks).filter(Tasks.id < 10)
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def equals():
    result = session.query(Tasks).filter(Tasks.id == 1)
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def not_equals():
    result = session.query(Tasks).filter(Tasks.id != 3)
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def like():
    result = session.query(Tasks).filter(Tasks.title.like('Buy%'))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def not_like():
    result = session.query(Tasks).filter(Tasks.title.not_like('Buy%'))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def contains():
    result = session.query(Tasks).filter(Tasks.title.contains('u'))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def startswith():
    result = session.query(Tasks).filter(Tasks.title.startswith('B'))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def endswith():
    result = session.query(Tasks).filter(Tasks.title.endswith('n'))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def in_():
    result = session.query(Tasks).filter(Tasks.id.in_([1,2]))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def not_in():
    result = session.query(Tasks).filter(Tasks.id.not_in([1,2]))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)

def and_():
    result = session.query(Tasks).filter(Tasks.id > 2, Tasks.title.like('Buy%'))
    for row in result:
        print("ID:",row.id, "Title:",row.title, "Description:",row.description, "Complete:",row.complete, "Created time::",row.timestamp, "User_id:",row.user_id)


if __name__ == "__main__":
    ic("------ show_all() ------")
    show_all()

    ic("------ greater_than() ------")
    greater_than()
    ic("------ less_than() ------")
    less_than()

    ic("------ equals() ------")
    equals()
    ic("------ not_equals() ------")
    not_equals()

    ic("------ like() ------")
    like()
    ic("------ not_like() ------")
    not_like()
    ic("------ contains() ------")
    contains()
    ic("------ startswith() ------")
    startswith()
    ic("------ endswith() ------")
    endswith()
    
    ic("------ in_() ------")
    in_()
    ic("------ not_in() ------")
    not_in()

    ic("------ and_() ------")
    and_()

    ic("------ end ------")
