from fastapi import APIRouter
from app.schemas.card_schema import Pessoa, CardCriado, MoverCardInput
from app.services import pipefy_service

router = APIRouter()

@router.get("/", tags=["Teste API"])
def test_API():
    return {"messase": "API rodando!"}

@router.post("/criar-pessoa", response_model=CardCriado, status_code=201, tags=["Criar card Pessoa"])
def criar_card_pessoa(pessoa: Pessoa):
    return pipefy_service.criar_card_pipefy(pessoa)

@router.delete("/deleter-pessoa/{card_id}", status_code=200, tags=["Deletar card Pessoa"])
def deletar_card_pessoa(card_id: str):
    return pipefy_service.deletar_card_pipefy(card_id)

@router.post("/mover-card/{card_id}", tags=["Mover card Pessoa"])
def mover_card(card_id: str, mover_input: MoverCardInput):
    return pipefy_service.mover_fase_card(card_id, mover_input.id_phase_destination)