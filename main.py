from api import *
import tempo

def main():
    # chama função de procurar processos na API
    dados_da_api = procurar_debitos()
    
    # Salva os dados em um arquivo JSON
    with open('dados_da_api.json', 'w') as arquivo:
        json.dump(dados_da_api, arquivo, indent=6)
     
    # Calcula o tempo e verifica os processos parados há mais de 48 horas
    processos_parados_72h = tempo.processos_parados(dados_da_api)

    # Imprime os processos parados há mais de 72 horas
    print("Processos parados há mais de 72 horas:", processos_parados_72h)
   
    user_id = "64b5c8e943c081004f45e66b" # id usuário Automação
    action_id = "Flow_09p801h"
    
    # Atribuir a tarefa para cada processo parado
    for processo in processos_parados_72h:
         tempo.atribuir_tarefa(processo["id"],user_id)
         comentar_debito(processo["process_id"])
         print(processo["id"])
         mudar_campo(processo["id"],action_id)

if __name__ == '__main__':
    main()
