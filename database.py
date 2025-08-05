#################
#    Imports    #
#################
from sqlmodel import SQLModel, create_engine, Session, Field
import models

#################
#    Engine     #
#################
# define rhe database file name
sqlite_file_name = "database.db"

# create a sqlite DB for development
sqlite_url = f"sqlite:///{sqlite_file_name}"

# create the database engine
engine = create_engine(sqlite_url, echo=True) # echo True for debugging

# the DB file wont be created until we execute the database.py
if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)  # Create the database tables
