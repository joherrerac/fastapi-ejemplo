from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    nombre: str
    apellido1: str
    apellido2: str
    rut: str