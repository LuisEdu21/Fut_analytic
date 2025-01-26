import sys
sys.path.append("config")
import functions_Soccer as cf
import bd as cd
import datetime
import asyncio
import mensageiro
import traceback
import os

loop = asyncio.get_event_loop()

while True:
    try:
        agora = datetime.datetime.now()

        if agora.weekday() not in [5, 6]:
            if agora.hour == 7 and agora.minute == 0:
                loop.run_until_complete(mensageiro.enviar_mensagem("Bot em funcionamento!"))
                cf.run()

            elif agora.hour == 23 and agora.minute == 30:
                loop.run_until_complete(mensageiro.enviar_mensagem("Atualizando resultado dos jogos!"))
                cf.game_of_the_day()
                cf.statistics()
                  
        else:
            if agora.hour == 5 and agora.minute == 0:
                loop.run_until_complete(mensageiro.enviar_mensagem("Bot em funcionamento!"))
                cf.run()

    except Exception as err:
        # Diretório onde os logs serão salvos
        pasta_log = "log"
        os.makedirs(pasta_log, exist_ok=True)  # Cria a pasta se não existir

        # Nome do arquivo de log com a data atual
        data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
        nome_arquivo = f"log_de_erros_{data_atual}.txt"

        # Caminho completo do arquivo de log
        caminho_arquivo = os.path.join(pasta_log, nome_arquivo)

        # Escreve o erro no arquivo de log
        with open(caminho_arquivo, "a") as log_file:
            # Horário atual para registrar o momento do erro
            horario_atual = datetime.datetime.now().strftime("%H:%M:%S")
            log_file.write(f"Horário: {horario_atual}\n")
            log_file.write("Erro ocorrido:\n")
            log_file.write(traceback.format_exc())  # Registra o rastreamento do erro
            log_file.write("\n-------------------------\n")  # Separador para facilitar a leitura

        
        agora = datetime.datetime.now()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(mensageiro.enviar_mensagem(f'Erro no analise_esportiva: {agora}'))
        pass