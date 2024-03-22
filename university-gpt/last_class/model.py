from sqlmodel import Relationship, SQLModel, Field



class TeamBase(SQLModel):
    name: str
    headquarter: str      


class Team(TeamBase,table=True):
    id: int = Field(default=None, primary_key=True)

    heroes: list["Heross"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass  

class TeamResponse(TeamBase):
    id: int

class TeamUpdate(TeamBase):
    name: str | None = None
    headquarter: str | None = None  



class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_key: str
    team_id: int | None = Field(default=None, foreign_key="team.id")

class Heross(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True,index=True)
    age: int | None = None

    team: Team = Relationship(back_populates='heroes')


class HeroCreate(HeroBase):
    age: int | None = None

class HeroResponse(HeroBase):
    id: int
    age: int | None = None

# model to update hero
class HeroUpdate(SQLModel):
     name: str | None = None
     secret_key: str | None = None
     age: int | None = None 


class HeroResponseWithTeam(HeroResponse):
    team: TeamResponse
