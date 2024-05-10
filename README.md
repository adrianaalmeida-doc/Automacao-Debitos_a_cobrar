# Automação Fluxo de Débitos á Cobrar 

## Descrição
Este é um script Python desenvolvido para automatizar a verificação e gestão de processos na API do HOlmes. Ele realiza as seguintes 
# tarefas:
Procurar Débitos na API: Utiliza uma função para buscar informações sobre os débitos na API e retorna os dados encontrados.
Salva os dados obtidos da API em um arquivo JSON chamado dados_da_api.json.
Verificar Processos Parados: Calcula o tempo de inatividade dos processos e identifica aqueles que estão parados há mais de 72 horas.
Atribui tarefas a usuários específicos para os processos parados há mais de 72 horas, realiza comentários e atualiza campos de ação.

## Libs
Python 3.x
Pacotes json ,requests, datetime, timedelta

## Instalação

Clone ou baixe este repositório para o seu ambiente local.
Execute o script Python main.py.
Os resultados serão impressos no terminal, incluindo os processos parados há mais de 72 horas e as ações realizadas.
bash
Copy code
python main.py

## Configuração
user_id: Substitua pelo ID do usuário para atribuição de tarefas.
action_id: Substitua pelo ID da ação a ser realizada nos processos.

## Notas
Este script foi desenvolvido para uso específico da  API do HOlmes. Certifique-se de adaptá-lo de acordo com suas necessidades e requisitos específicos. 

