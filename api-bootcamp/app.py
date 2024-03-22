from typing import Optional
from sqlmodel import SQLModel, create_engine, Field, Session, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


database_connection_str=""
engine=create_engine(database_connection_str, echo=True)

def create_hero():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson", age=80)
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador" ,age=30)
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Super-Man", secret_name="Henry Cavill", age=28)
    hero_5 = Hero(name="Bat-Man", secret_name="Christan Bale", age=33)

    session = Session(engine)

    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.add(hero_4)
    session.add(hero_5)

    session.commit()  


def get_hero():
    session = Session(engine)
    statement=select(Hero).where(Hero.name == "Bat-Man")
    # statement=select(Hero).where(Hero.name == "Bat-Man").where(Hero.age==33).limit(1)
    # statement=select(Hero.name == "Bat-Man").offset(4).limit(2)
    result=session.exec(statement)
    print(result.all())
    # print(result.one())
    # print(result.first())
    # for hero in result:
    #     print("print individual")
    #     print(hero.name)


def update_heroes():
    session = Session(engine)
    statement=select(Hero).where(Hero.name == "Deadpond")
    result=session.exec(statement).first()
    print(result)
    result.age=56
    session.add(result)
    session.commit()
    session.close()
    print("updated age")
    print(result)    


def delete_hero():
    session = Session(engine)
    statement=select(Hero).where(Hero.id == 11)
    result=session.exec(statement).first()
    print(result)
    session.delete(result)
    session.commit()
    session.close()    


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    # create_db_and_tables()
    # create_hero()
    # get_hero()
    # # update_heroes()
    delete_hero()
