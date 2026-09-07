from pydantic import BaseModel

class AlarmRequest(BaseModel):
    time: str
    day: str
    message: str
    turn_on: bool

class AlarmUpdateRequest(BaseModel):
    id: int
    time: str
    day: str
    message: str
    turn_on: bool

class AlarmDeleteRequest(BaseModel):
    id: int