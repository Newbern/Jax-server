from pydantic import BaseModel

class AlarmRequest(BaseModel):
    time: str
    day: str
    message: str
    repeat: bool