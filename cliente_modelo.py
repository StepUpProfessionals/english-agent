from pydantic import BaseModel, EmailStr, Field

class Cliente(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)
    email: EmailStr
    edad: int = Field(ge=0, le=120)
