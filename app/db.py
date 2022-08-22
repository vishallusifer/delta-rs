from typing import Optional
from sqlmodel import Field, Session, create_engine 
#ToDo: need to make it environment specific, also password cannot be exposed. w
DATABASE_URL = "mysql+mysqlconnector://admin:adminadmin@delta.cv05ixcxspwi.us-east-2.rds.amazonaws.com/delta"

engine = create_engine(DATABASE_URL, echo=False)

session = Session(bind=engine)        



