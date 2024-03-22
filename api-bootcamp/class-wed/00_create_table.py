from typing import Optional
from sqlmodel import SQLModel, create_engine, Field, Session, select
from dotenv import load_dotenv,find_dotenv
from os import getenv


_bool = load_dotenv(find_dotenv())

class Team(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str 
    headquater: str 


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")    

postgres_url = getenv("POSTGRES_URL")    
engine=create_engine(postgres_url,echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables

if __name__ == '__main__':
    main()        