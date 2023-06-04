import sys
sys.path.append("config")
import funcoes as cf
import bd as cd

try:
    cd.criar_Tabela()
    cf.Bundesliga()
    cf.brasileirao_Serie_A()
    cf.brasileirao_Serie_B()

except Exception as err:
    print("Erro", err)
