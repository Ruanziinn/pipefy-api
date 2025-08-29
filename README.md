### Lista de Hobbies
Teatro, Música, Cinema, Esportes, Leitura, Viagem, Artes

### Cidades (Pode colocar o nome, essa API fica responsável por pegar o ID e enviar a API do Pipefy)
Caucaia, Maranguape, Fortaleza, Maracanaú, Eusébio

### Criação de Card
```graphql
mutation {
  createCard(input: {
    pipe_id: "PIPE_ID",
    title: "NOME",
    fields_attributes: [
      {field_id: "nome", field_value: "NOME"},
      {field_id: "data_de_nascimento", field_value: "2025-08-29"},
      {field_id: "cpf", field_value: "CPF"},
      {field_id: "telefone", field_value: "TELEFONE"},
      {field_id: "data", field_value: "2025-08-29T11:01:00"},
      {field_id: "sexo", field_value: ["SEXO"]},
      {field_id: "hobbies", field_value: ["Cinema", "Esportes"]},
      {field_id: "cidade", field_value: ["ID_DO_CONECTOR_DA_CIDADE"]}
    ]
   }) {
     card {
       id
       title
       url
     }
   }
}
```

### Deletar Card

```graphql
mutation {
  deleteCard(input: {id: "ID_DO_CARD"}) {
    success
  }
}
```

### Mover Card

```graphql
mutation {
  moveCardToPhase(input: {
    card_id: "ID_DO_CARD",
    destination_phase_id: "ID_DA_FASE_DE_DESTINO"
  }) {
    card {
      id
      current_phase { id }
    }
  }
}
```