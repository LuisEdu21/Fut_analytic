import sys
sys.path.append("config")
import funcoes as cf
import bd as cd

try:
    cd.criar_Tabela()
    cf.Premier_League()
    cf.Serie_A_TIM()
    cf.La_liga()
    cf.Bundesliga()
    cf.Ligue_1()
    cf.brasileirao_Serie_A()
    cf.brasileirao_Serie_B()
    #teste Webhook

except Exception as err:
    print("Erro", err)
