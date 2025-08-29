from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class Pessoa(BaseModel):
    nome: str
    data_de_nascimento: Optional[date] = None 
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    data_envio: Optional[datetime] = None
    sexo: Optional[str] = None
    hobbies: Optional[str] = None
    cidade: str

class CardCriado(BaseModel):
    id: str
    title: str
    url: str

class MoverCardInput(BaseModel):
    id_phase_destination: str
