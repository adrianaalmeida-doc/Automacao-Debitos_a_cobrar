from api import *
from datetime import datetime, timedelta

# Calculando tempo e transformando em hora
def calcular_tempo(tempo_inicial, tempo_final):
    delta = tempo_final - tempo_inicial
    return delta.total_seconds() / 3600  

def processos_parados(dados):
    processos_parados_72h = []
    now = datetime.utcnow()
    
    for doc in dados.get('docs', []):
        updated_at = datetime.strptime(doc['updated_at'], "%Y-%m-%dT%H:%M:%S.%fZ") # convertendo a string em um objeto date time
        diferenca = calcular_tempo(updated_at, now)  
       
        
        if diferenca > 72:
            processos_parados_72h.append(doc)
            print(diferenca)

    return processos_parados_72h


