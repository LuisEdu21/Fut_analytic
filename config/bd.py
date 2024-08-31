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

def close_connection(conn,cursor):
    
    cursor.close()
    conn.close()

    return

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
        conexao.commit()
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

def fetch_id_country(cursor,name):

    sql = f"""select id from futebol.country c where "name" = '{name}'"""
    cursor.execute(sql)

    result = cursor.fetchall()
    
    id_country = result[0][0]

    return id_country

def insert_league(conn, cursor, id, name, type, logo, id_country):

    sql = f"""select * from futebol.league l where id = '{id}'"""
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:

        id_country = fetch_id_country(cursor,id_country)

        insert = """INSERT INTO futebol.league (id, "name", "type", logo, id_country) VALUES(%s, %s, %s, %s, %s);"""
        cursor.execute(insert,(id,name,type,logo,id_country))
        conn.commit()
    else:
        pass
    
    return

def insert_country(conn,cursor,name, code, flag):

    sql = f"""select * from futebol.country c where "name" = '{name}'"""
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:
        insert = """INSERT INTO futebol.country ("name", code, flag) VALUES(%s, %s, %s);"""
        cursor.execute(insert,(name, code, flag))
        conn.commit()
    else:
        pass

    return 