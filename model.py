from pydantic import BaseModel
from fastapi import Path

# User Login Model
class UserLogin(BaseModel):
    email: str = Path(min_length=3, max_length=20)
    password: str = Path(min_length=6, max_length=20)

# User Signup Model
class UserSignup(BaseModel):
    email: str = Path(min_length=3, max_length=20)
    password: str = Path(min_length=6, max_length=20)
    username: str = Path(min_length=3, max_length=20)

# Sensor Data Model
class SensorData(BaseModel):
    id: int = Path(gt=0, description="Sensor Data ID")
    timestamp: str
    temperature: float
    humidity: float