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

def criar_Tabela():
    conexao = conexao_Com_Banco()

    SQL_Criacao_Tabela = """CREATE TABLE public.tabela_fut (
	liga varchar NULL,
	colocacao int4 NULL,
	clube varchar NULL,
	pts int4 NULL,
	pj int4 NULL,
	vit int4 NULL,
	e int4 NULL,
	der int4 NULL,
	gm int4 NULL,
	gc int4 NULL,
	sg int4 NULL,
	datahora timestamp NULL)"""
    
    cursor = conexao.cursor()

    with open("config/Tabela.txt", "r") as arquivo:
        resultado = arquivo.read()

    if resultado == 'N':
        cursor.execute(SQL_Criacao_Tabela)
        #conexao.commit()
        with open("config/Tabela.txt", "w") as arquivo:
            arquivo.write("S")
    else:
        print('Tabela já existe')

    return print('Finalizado processo...')

def Inserirtime(liga,colocacao,clube,pts,pj,vit,empate,der,gm,gc,sg):
    con = conexao_Com_Banco()
    cur = con.cursor()
    print("connection established")
    sql = "insert into tabela_fut (liga,colocacao,clube,pts,pj,vit,e,der,gm,gc,sg,datahora) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',now())".format(liga,colocacao,clube,pts,pj,vit,empate,der,gm,gc,sg)
    cur.execute(sql)
    con.commit()
    print ("Conclusion")
