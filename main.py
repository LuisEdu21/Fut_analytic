import sys
sys.path.append("config")
import funcoes as cf
import bd as cd
import datetime
import asyncio
import mensageiro
import traceback

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
                  
        else:
            if agora.hour == 5 and agora.minute == 0:
                loop.run_until_complete(mensageiro.enviar_mensagem("Bot em funcionamento!"))
                cf.run()

    except Exception as err:
        with open("log_de_erros.txt", "a") as log_file:
            log_file.write("Ocorreu um erro:\n")
            log_file.write(traceback.format_exc())  # Isso grava a mensagem completa do erro no arquivo
            log_file.write("\n-------------------------\n")  # Separador para facilitar a leitura

        agora = datetime.datetime.now()
        loop.run_until_complete(mensageiro.enviar_mensagem(f'Erro no BotBet, horario do erro: {agora}'))
        pass
