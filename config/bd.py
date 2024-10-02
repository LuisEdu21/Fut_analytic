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

    sql = f"""select l.id from futebol.league l 
            left join futebol.country c on l.id_country = c.id
            where "type" = 'League' and c.id <> '1' and l.id in ('39','61','71','72','78','88','94','135','140')
            order by l.id;"""
    cursor.execute(sql)

    result = cursor.fetchall()
    
    return result

def search_leagues_team(cursor):

    sql = f"""select l.id from futebol.league l 
            left join futebol.country c on l.id_country = c.id
            where l.id in ('2','3','11','13','39','45','48','61','71','72','78','88','94','135','140')
            order by l.id;"""
    cursor.execute(sql)

    result = cursor.fetchall()
    
    return result

def search_cup(cursor):

    sql = f"""select l.id, l."name" from futebol.league l 
            left join futebol.country c on l.id_country = c.id
            where "type" = 'Cup' and l.id in ('2','3','11','13','45','48')
            order by l.id;"""
    cursor.execute(sql)

    result = cursor.fetchall()
    
    return result

def search_for_games_of_the_day(cursor):

    sql = f"""select g.id, t.name, t2."name", to_char(g."date",'HH:mi') from futebol.game g 
            left join futebol.team t on g.id_team_home = t.id 
            left join futebol.team t2 on g.id_team_away = t2.id 
            where date::date = current_date and t.name is not null
           order by g."date" asc;"""
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
                    SET id_team= %s, point= %s, goalsdiff= %s, form= %s, status= %s, description= %s, played= %s, win= %s, draw= %s, lose= %s, gf= %s, ga= %s where id_league= %s and "rank"= %s and season = %s """
        cursor.execute(update,(id_team,point,goalsdiff,form,status,description,played,win,draw,lose,gf,ga,id_league,rank,season))
        conn.commit()

        pass

    return

def insert_game(conn,cursor,id,date,id_venue,id_league,season,round,id_team_home,id_team_away,goals_home,goals_away):
   
    sql = f"""select * from futebol.game g where id = '{id}';"""
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:
        insert = """INSERT INTO futebol.game (id, "date", id_venue, id_league, season, round, id_team_home, id_team_away, goals_home, goals_away)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        cursor.execute(insert,(id,date, id_venue, id_league, season, round, id_team_home, id_team_away, goals_home, goals_away))
        conn.commit()
    else:
        update = """UPDATE futebol.game SET goals_home=%s, goals_away=%s where id=%s"""
        cursor.execute(update,(goals_home, goals_away, id))
        conn.commit()

        pass

    return

def inset_predictions(conn,cursor,id_game,winner_id,winner_comment,win_or_draw,under_over,goals_home,goals_away,advice,percent_home,percent_draw,percent_away,id_league):

    sql = f"""select * from futebol.predictions p where id_game = '{id_game}';"""
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) == 0:
        insert = """INSERT INTO futebol.predictions (id_game, winner_id, winner_comment, win_or_draw, under_over, goals_home, goals_away, advice, percent_home, percent_draw, percent_away, id_league)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        cursor.execute(insert,(id_game,winner_id,winner_comment,win_or_draw,under_over,goals_home,goals_away,advice,percent_home,percent_draw,percent_away,id_league))
        conn.commit()
    else:
        pass

    return

def create_table():

    connection = connection_with_bank()

    sql = [
    """CREATE SCHEMA futebol AUTHORIZATION postgres;""",
    """CREATE TABLE futebol.country (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL,code VARCHAR(10),flag VARCHAR(255));""",
    """CREATE TABLE futebol.league (id SERIAL PRIMARY KEY,name VARCHAR(255) NOT NULL,type VARCHAR(50),logo VARCHAR(255),id_country INT,FOREIGN KEY (id_country) REFERENCES futebol.country(id));""",
    """CREATE TABLE futebol.team (id SERIAL PRIMARY KEY,name VARCHAR(255) NOT NULL,code VARCHAR(10),country VARCHAR(50), founded INT,national BOOLEAN,logo VARCHAR(255));""",
    """CREATE TABLE futebol.stadium (id SERIAL PRIMARY KEY,name VARCHAR(255) NOT NULL,address VARCHAR(255),city VARCHAR(255),country VARCHAR(50),capacity INT,surface VARCHAR(50),image VARCHAR(255),id_team INT,FOREIGN KEY (id_team) REFERENCES futebol.team(id));""",
    """CREATE TABLE futebol.game (id SERIAL PRIMARY KEY,date DATE NOT NULL,id_venue INT,id_league INT,season VARCHAR(10),round VARCHAR(255),id_team_home INT,id_team_away INT,goals_home INT,goals_away INT,FOREIGN KEY (id_league) REFERENCES futebol.league(id),FOREIGN KEY (id_team_home) REFERENCES futebol.team(id),FOREIGN KEY (id_team_away) REFERENCES futebol.team(id));""",
    """CREATE TABLE futebol.table_leagues (id_league INT,id_team INT,rank INT,point INT,goalsdiff INT,form VARCHAR(255),status VARCHAR(50),description TEXT,played INT,win INT,draw INT,lose INT,gf INT,ga INT,season INT,PRIMARY KEY (id_league, id_team),FOREIGN KEY (id_league) REFERENCES futebol.league(id),FOREIGN KEY (id_team) REFERENCES futebol.team(id));""",
    """CREATE TABLE futebol.predictions (id_game INT,winner_id INT,winner_comment TEXT,win_or_draw BOOLEAN,under_over INT,goals_home INT,goals_away INT,advice TEXT,percent_home DECIMAL(5, 2),percent_draw DECIMAL(5, 2),percent_away DECIMAL(5, 2),id_league INT,green BOOLEAN,PRIMARY KEY (id_game),FOREIGN KEY (id_game) REFERENCES futebol.game(id),FOREIGN KEY (id_league) REFERENCES futebol.league(id));"""
    ]
    
    cursor = connection.cursor()

    with open("config/Tabela.txt", "r") as arquivo:
        resultado = arquivo.read()

    if resultado == 'N':
        for consulta in sql:
            cursor.execute(consulta)
            connection.commit()
        with open("config/Tabela.txt", "w") as arquivo:
            arquivo.write("S")
    else:
        print('Tabela já existe')

    close_connection(connection,cursor)

    return print('Finalizado processo...')