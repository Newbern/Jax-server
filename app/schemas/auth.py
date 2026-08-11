from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str
    device_type: str

class DeviceLoginRequest(BaseModel):
    device_id: str
    api_key: str

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    device_type: str



