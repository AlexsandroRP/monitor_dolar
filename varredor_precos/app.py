import schedule
from time import sleep
import os

# Mudar uma vez para o diretório que contém o prejeto scrapy
print(os.getcwd()) # printa localização atual
os.chdir('varredor_precos') # muda de diretório para a pasta 'varredor_precos'
print(os.getcwd())

# Criar uma função que será executada periodicamente
def rodar_botprecos():
    os.system('scrapy crawl dolarbot') # Rodar o bot
# Agendar essa execução
schedule.every(1).minutes.do(rodar_botprecos)
print(str(schedule.next_run())) # imprime quando o próximo script será executado
# Colocar esse agendamento na fila
while True:
    schedule.run_pending()
    sleep(1)