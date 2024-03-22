from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import SQLModel, create_engine, Session, select
from model import HeroCreate,HeroResponse,Heross,HeroUpdate,Team,TeamCreate,TeamResponse,TeamUpdate,HeroResponseWithTeam

from typing import Annotated



DB_URL = ""

engine=create_engine(DB_URL,echo=True)    

def create_table():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

def get_deb():
    with Session(engine) as session:
        yield session 
    

@app.on_event("startup")
def on_startup():
    create_table()


# get all hero
@app.get("/heros", response_model=list[Heross])
def get_heros(session:Annotated[Session, Depends(get_deb)], offset:int=Query(default=0,le=4), limit:int=Query(default=2,le=4)):
        heros = session.exec(select(Heross).offset(offset).limit(limit)).all()
        return heros



  # post change in hero
@app.post("/heros", response_model=HeroResponse)
def create_heros(hero:HeroCreate,db:Annotated[Session,Depends(get_deb)]):
       hero_to_insert=Heross.model_validate(hero)
       db.add(hero_to_insert)
       db.commit()
       db.refresh(hero_to_insert)
       return hero_to_insert



# get single hero by id
@app.get('/heros/{heros.id}',response_model=HeroResponseWithTeam)
def get_hero_by_id(hero_id:int, session:Annotated[Session,Depends(get_deb)]):
     hero = session.get(Heross,hero_id)
     if not hero:
          raise HTTPException(status_code=404, detail="Hero not found")
     print(hero.team)
     return hero



# update hero
@app.patch('/heros/{heros.id}',response_model=HeroResponse)
def update_hero(hero_id:int, hero_data:HeroUpdate, session:Annotated[Session,Depends(get_deb)]):
     
    hero = session.get(Heross,hero_id)
    if not hero:
          raise HTTPException(status_code=404, detail="Hero not found")
    print('hero in db',hero)
    print('data from client',hero_data)

    hero_dict_data = hero_data.model_dump(exclude_unset=True)
    print("hero_dict_data",hero_dict_data)
    
    for key,value in hero_dict_data.items():
         setattr(hero,key,value)

    session.add(hero)
    session.commit()
    session.refresh(hero)  
    return hero   

# hero delete
@app.delete('/heros/{heros.id}')
def delete_hero(hero_id:int, session:Annotated[Session,Depends(get_deb)]):
     
    hero = session.get(Heross,hero_id)
    if not hero:
          raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {'message':'hero deleted successfully'}



   
# get teams
@app.get("/teams",response_model=list[Team])
def get_teams(session:Annotated[Session, Depends(get_deb)], offset:int=Query(default=0,le=4), limit:int=Query(default=2,le=4)):
     teams = session.exec(select(Team).offset(offset).limit(limit)).all()
     return teams

# post teams insert values in teams 
@app.post("/teams", response_model=TeamResponse)
def create_teams(team:TeamCreate,db:Annotated[Session,Depends(get_deb)]):
       teams_to_insert=Team.model_validate(team)
       db.add(teams_to_insert)
       db.commit()
       db.refresh(teams_to_insert)
       return teams_to_insert


# get teams by id
@app.get('/teams/{teams.id}',response_model=TeamResponse)
def get_team_by_id(team_id:int, session:Annotated[Session,Depends(get_deb)]):
     team = session.get(Team,team_id)
     if not team:
          raise HTTPException(status_code=404, detail="team not found")
     return team


# update team
@app.patch('/teams/{teams.id}',response_model=TeamResponse)
def update_hero(team_id:int, team_data:TeamUpdate, session:Annotated[Session,Depends(get_deb)]):
     
    team = session.get(Team,team_id)
    if not team:
          raise HTTPException(status_code=404, detail="team not found")
    print('team in db',team)
    print('data from client',team_data)

    team_dict_data = team_data.model_dump(exclude_unset=True)
    print("team_dict_data",team_dict_data)
    
    for key,value in team_dict_data.items():
         setattr(team,key,value)

    session.add(team)
    session.commit()
    session.refresh(team)  
    return team   

# team delete
@app.delete('/teams/{teams.id}')
def delete_team(team_id:int, session:Annotated[Session,Depends(get_deb)]):
     
    team = session.get(Team,team_id)
    if not team:
          raise HTTPException(status_code=404, detail="team not found")
    session.delete(team)
    session.commit()
    return {'message':'team deleted successfully'}



