import psycopg2 as pg
import os 
from dotenv import load_dotenv

load_dotenv()

def conexao_Com_Banco():
    conexao = pg.connect(host = os.getenv('host_DB'), 
                database=os.getenv('database_DB'),
                user=os.getenv('user_DB'), 
                password=os.getenv('pass_DB'))
    return conexao


def Inserirtime(liga,colocacao,clube,pts,pj,vit,empate,der,gm,gc,sg):
    con = conexao_Com_Banco()
    cur = con.cursor()
    print("connection established")
    sql = "insert into tabela_fut (liga,colocacao,clube,pts,pj,vit,e,der,gm,gc,sg,datahora) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',now())".format(liga,colocacao,clube,pts,pj,vit,empate,der,gm,gc,sg)
    cur.execute(sql)
    con.commit()
    print ("Conclusion")



