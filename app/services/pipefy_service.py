import requests
import json
from fastapi import HTTPException

from app.configuration.config import PIPEFY_URL, PIPE_ID, CIDADES, FASE_FINAL_ID, headers
from app.schemas.card_schema import Pessoa, CardCriado, MoverCardInput

def criar_card_pipefy(pessoa: Pessoa) -> CardCriado:
    card_title = f"Cadastro de {pessoa.nome}"

    nome_field = f'{{field_id: "nome", field_value: "{pessoa.nome}"}}'
    
    fields_parts = [nome_field]
    
    if pessoa.data_de_nascimento is not None:
        fields_parts.append(f'{{field_id: "data_de_nascimento", field_value: "{pessoa.data_de_nascimento.isoformat()}"}}')
    
    if pessoa.cpf is not None:
        fields_parts.append(f'{{field_id: "cpf", field_value: "{pessoa.cpf}"}}')
        
    if pessoa.telefone is not None:
        fields_parts.append(f'{{field_id: "telefone", field_value: "{pessoa.telefone}"}}')

    if pessoa.data_envio is not None:
        fields_parts.append(f'{{field_id: "data", field_value: "{pessoa.data_envio.isoformat()}"}}')

    if pessoa.sexo is not None:
        fields_parts.append(f'{{field_id: "sexo", field_value: ["{pessoa.sexo}"]}}')

    if pessoa.hobbies is not None:
        hobbies_lista = [hobby.strip() for hobby in pessoa.hobbies.split(',')]
        hobbies_formatado = json.dumps(hobbies_lista)
        fields_parts.append(f'{{field_id: "hobbies", field_value: {hobbies_formatado}}}')

    cidade_id = CIDADES.get(pessoa.cidade)
    if not cidade_id:
        raise HTTPException(status_code=400, detail=f"Cidade inválida: '{pessoa.cidade}'.")
    fields_parts.append(f'{{field_id: "cidade", field_value: ["{cidade_id}"]}}')

    fields_body = ", ".join(fields_parts)

    mutation = f"""
    mutation {{
      createCard(input: {{
        pipe_id: "{PIPE_ID}",
        title: "{card_title}",
        fields_attributes: [{fields_body}]
       }}) {{
         card {{ 
           id
           title
           url
         }}
       }}
    }}
    """
    payload = {"query": mutation}

    try:
        response = requests.post(PIPEFY_URL, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        if "errors" in response_data:
            raise HTTPException(status_code=400, detail=response_data["errors"])
        
        card_data = response_data["data"]["createCard"]["card"]
        return CardCriado(**card_data)

    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=502, detail=f"Erro de comunicação com o pipefy: {http_err.response.text}")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro interno: {err}")
    
def deletar_card_pipefy(card_id: int) -> dict:
    mutation = f"""
    mutation {{ 
        deleteCard(input: {{id: "{card_id}"}}) {{
            success
        }}
    }}
    """
    payload = {"query": mutation}

    try:
        response = requests.post(PIPEFY_URL, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        if "errors" in response_data:
            error_message = response_data["errors"][0]["message"]
            raise HTTPException(status_code=404, detail=f"Erro ao deletar card: {error_message}")
        
        success = response_data.get("data", {}).get("deleteCard", {}).get("success", False)

        if success:
            return {"mensagem": f"Card {card_id} deletado com sucesso."}
        else:
            raise HTTPException(status_code=400, detail="A API do Pipefy não confirmou se foi deletado.")

    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=502, detail=f"Erro de comunicação com o Pipefy: {http_err.response.text}")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro interno: {err}")
    

def mover_fase_card(card_id: str, id_phase_destination: str) -> dict:
    mutation = f"""
    mutation {{
      moveCardToPhase(input: {{
        card_id: "{card_id}", 
        destination_phase_id: "{id_phase_destination}"
      }}) {{
        card {{
          id
          current_phase {{ id }}
        }}
      }}
    }}
    """
    payload = {"query": mutation}

    try:
        response = requests.post(PIPEFY_URL, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        if "errors" in response_data:
            error_message = response_data["errors"][0]["message"]
            raise HTTPException(status_code=400, detail=f"Erro ao mover card: {error_message}")
            
        if id_phase_destination == FASE_FINAL_ID:
            return {"status": "concluido", "mensagem": f"Card {card_id} movido para a fase final."}
        else:
            return {"status": "movido", "mensagem": f"Card {card_id} movido para a fase {id_phase_destination}."}

    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=502, detail=f"Erro de comunicação com o Pipefy: {http_err.response.text}")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro interno: {err}")    