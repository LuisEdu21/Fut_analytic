import psycopg2 as pg
import os 
from dotenv import load_dotenv

load_dotenv()

def connection_with_bank():
    conexao = pg.connect(host = os.getenv('host_DB'), 
                database=os.getenv('database_DB'),
                user=os.getenv('user_DB'), 
                password=os.getenv('pass_DB'))
    return conexao

def close_connection(conn,cursor):
    
    cursor.close()
    conn.close()

    return

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

def insert_team(conn,cursor,id, name, code,country,founded,national,logo):

    sql = f"""select * from futebol.team t where id = '{id}'"""
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:
        insert = """INSERT INTO futebol.team (id, "name", code, country, founded, "national", logo) VALUES(%s, %s, %s, %s, %s, %s, %s);"""
        cursor.execute(insert,(id, name, code,country,founded,national,logo))
        conn.commit()
    else:
        pass

    return 

def insert_stadium(conn,cursor,id, name, address, city, country, capacity, surface, image, id_team):

    if id == None:
        pass
    else:
        sql = f"""select * from futebol.stadium s where id = '{id}'"""
        cursor.execute(sql)
        result = cursor.fetchall()

        if len(result) == 0:
            insert = """INSERT INTO futebol.stadium (id, "name", address, city, country, capacity, surface, image, id_team) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            cursor.execute(insert,(id, name, address, city, country, capacity, surface, image, id_team))
            conn.commit()
        else:
            pass

    return 

def search_leagues(cursor):

    sql = f"""SELECT id
            FROM (
                SELECT 
                    l.*, 
                    ROW_NUMBER() OVER (PARTITION BY l.id_country ORDER BY l.id) AS rn
                FROM 
                    futebol.league l
            ) subquery
            WHERE rn = 1 and id_country <> 1
            ORDER BY id_country, id
            limit 85;"""
    cursor.execute(sql)

    result = cursor.fetchall()
    
    return result

def search_leagues_table(cursor):

    sql = f"""select l.id from futebol.league l 
            left join futebol.country c on l.id_country = c.id
            where "type" = 'League' and c.id <> '1' and l.id in ('61','71','39','78','135','89','94','140')
            order by l.id;"""
    cursor.execute(sql)

    result = cursor.fetchall()
    
    return result

def insert_table(conn,cursor,id_league,rank,id_team,point,goalsdiff,form,status,description,played,win,draw,lose,gf,ga,season):
   
    sql = f"""select * from futebol.table_leagues tl where id_league = '{id_league}' and season = '{season}' and rank = '{rank}';"""
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:
        insert = """INSERT INTO futebol.table_leagues (id_league, "rank", id_team, point, goalsdiff, form, status, description, played, win, draw, lose, gf, ga, season)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        cursor.execute(insert,(id_league,rank,id_team,point,goalsdiff,form,status,description,played,win,draw,lose,gf,ga,season))
        conn.commit()
    else:
        update = """UPDATE futebol.table_leagues
                    SET id_team=%s, point=%s, goalsdiff=%s, form=%s, status=%s, description=%s, played=%s, win=%s, draw=%s, lose=%s, gf=%s, ga=%s where id_league=%s and "rank"= %s and season= %s;"""
        cursor.execute(update,(id_team,point,goalsdiff,form,status,description,played,win,draw,lose,gf,ga,id_league,rank,season))
        conn.commit()

        pass

    return

def criar_Tabela():
    conexao = connection_with_bank()

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