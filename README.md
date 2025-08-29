# API de Integração com Pipefy

### Tecnologias
- Python 3.10+
- FastAPI

## Descrição
Esta é uma API RESTful desenvolvida em Python com FastAPI. O projeto funciona como uma camada de serviço (ou wrapper) sobre a API GraphQL do Pipefy, com o objetivo de simplificar as operações de CRUD para cards.

A API abstrai a complexidade do GraphQL, oferecendo endpoints intuitivos e adicionando lógicas de negócio customizadas, como a validação de dados e a sinalização de status em fases específicas do processo.

### Funcionalidades
- Criação (Create): Criação de novos cards de "Pessoa".
- Atualização (Update): Movimentação de cards entre as fases do pipe.
- Deleção (Delete): Exclusão de cards.

# Endpoints da API
## Criar um Novo Card de Pessoa
- Método: POST
- Path: /cards/criar-pessoa
- Nome e Cidade aqui são OBRIGATÓRIOS. Temos uma lista de hobbies e cidades.
#### Lista de Hobbies
Teatro, Música, Cinema, Esportes, Leitura, Viagem, Artes

#### Cidades (Pode colocar o nome, essa API fica responsável por pegar o ID e enviar a API do Pipefy)
Caucaia, Maranguape, Fortaleza, Maracanaú, Eusébio

- Corpo da Requisição (Exemplo):
```json
{
  "nome": "Ruan Ripardo",
  "data_de_nascimento": "2025-08-29",
  "cpf": "123.456.789-00",
  "telefone": "85911223344",
  "data_envio": "2025-08-29T19:35:09.971Z",
  "sexo": "Masculino",
  "hobbies": "Cinema, Esportes",
  "cidade": "Fortaleza"
}
```
- Resposta de Sucesso (201 Created):
```json
{
  "id": "12345678",
  "title": "Ruan Ripardo",
  "url": "https://app.pipefy.com/pipes/PIPE_ID/cards/12345678"
}
```

## Mover um Card para Outra Fase
- Método: POST
- Path: /cards/mover-card/{card_id}
- Parâmetro: card_id (string) - O ID do card a ser movido.
- Corpo da Requisição (Exemplo):
```json
{
  "id_fase_destino": "ID_DA_FASE_DE_DESTINO_AQUI"
}
```
- Resposta de Sucesso (200 OK):
```json
{
  "status": "movido",
  "mensagem": "Card 12345678 movido para a fase ID_DA_FASE_DE_DESTINO_AQUI."
}
```
  Se movido para a fase final, a resposta será {"status": "concluido", ...}.

## Deletar um Card
- Método: DELETE
- Path: /cards/deletar-pessoa/{card_id}
- Parâmetro: card_id (string) - O ID do card a ser deletado.
- Resposta de Sucesso (200 OK):
```json
{
  "mensagem": "Card 12345678 deletado com sucesso."
}
```


