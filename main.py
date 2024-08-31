import sys
sys.path.append("config")
import funcoes as cf
import bd as cd

try:
    cf.league_treatment()

except Exception as err:
    print("Erro", err)
