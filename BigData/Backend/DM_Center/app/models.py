from pydantic import BaseModel

# Modelo de datos:

class User(BaseModel):
    id: int
    name: str
    age: int
    profesion: str
