import sys
sys.path.append("config")
import funcoes as cf
import bd as cd

try:
    cd.criar_Tabela()

except Exception as err:
    print("Erro", err)
