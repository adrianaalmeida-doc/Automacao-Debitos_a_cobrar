import json
import requests
from dotenv import dotenv_values
from datetime import datetime
config = dotenv_values(".env")


def procurar_debitos():
  
    url = "https://app-api.holmesdoc.io/v2/search"
    headers = {'Content-Type': 'application/json', 'api_token': config.get("API_TOKEN")}
    payload={
   "query":{
      "from":0,
      "size":50,
      "context":"search_task",
      "sort":"updated_at",
      "order":"desc",
      "groups":[
         {
            "terms":[
               {
                  "name":"Fluxos",
                  "value":"64876deb0770e4009d2091fd",
                  "type":"is",
                  "filter":"HProcessFilter",
                  "field":"template_id",
                  "label":"DEBITOS A COBRAR"
               },
               {
                  "field":"status",
                  "label":"Aberto",
                  "name":"Situação da tarefa",
                  "type":"is",
                  "value":"opened",
                  "filter":"HProcessStatusFilter",
                  "nested":"false"
               },
               {
                  "field":"task_id",
                  "name":"Tarefa",
                  "type":"terms",
                  "value":[
                     "Activity_0bj5r5h"
                  ],
                  "filter":"HTaskFilter",
                  "label":"Aguardando Resposta do Gerente",
                  "nested":"false",
                  "id":"7b04d110-0efe-11ef-b153-51a06ee60b77"
               }
            ],
            "not_used":"false"
         }
      ]
   }
}
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    try:
        resposta = json.loads(response.text)
    except Exception as e:
        print("Erro de decodificação JSON:", e)
        resposta = {} 
    return resposta


def comentar_debito(process_id):
    url = f"https://app-api.holmesdoc.io/v1/processes/{process_id}/comments"
    headers = {'Content-Type': 'application/json', 'api_token': config.get("API_TOKEN")}
    payload ={
              "id":None,
              "message":"Processo enviado para cobrança! Motivo: processo parado há mais de 72 horas.\n",
              "mentions":[]
             }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
  
    if response.status_code == 200 or 201 :
        print("Comentário adicionado com sucesso.")
    else:
        print(f"Erro ao adicionar comentário. Status: {response.status_code}")

    
def atribuir_tarefa(task_id, user_id):
    
    url=f"https://app-api.holmesdoc.io/v1/tasks/{task_id}/assign" # id da tarefa : 663cd72a686219008bee82a3 (aguardando gerente)
    payload = { 
            "user_id":user_id} # id automação
    
    headers = {'Content-Type': 'application/json', 'api_token': config.get("API_TOKEN")}
    print("Realizando a requisição para atribuir tarefa  ao usuário Automação")
    request = requests.put(url, headers=headers, data=json.dumps(payload))
    if request.status_code ==  200 or 204:
        print(f"TaskID {task_id} atribuída ao usuário Automação")
    else:
        print(f"Task não atribuída. Erro: {request.text}, Status: {request.status_code}")

        
    return request    
def mudar_campo(task_id, action_id):
     
    url =  f"https://app-api.holmesdoc.io/v1/tasks/{task_id}/action"
    headers = {'Content-Type': 'application/json', 'api_token': config.get("API_TOKEN")}
    payload ={ 
      "task":{
      "action_id": action_id,
      "property_values":[
         {
            "id":"3152ee20-0956-11ee-b46f-29fa9fe6e0a9",
            "value":"64876fc384576e009df7127c",
            "text":"Enviar para Central de Cobrança (Com Bloqueio do Cliente)"
         }
      ],
      "confirm_action":"false"
   }
    }
    request = requests.post(url, headers=headers, data=json.dumps(payload))

   
    if request.status_code == 200 or 204:
        print(f"Processo {task_id} Enviado para Cobrança")
    else:
        print(f"Task não alterada Erro: {request.text}, Status: {request.status_code}")

        
    return request

