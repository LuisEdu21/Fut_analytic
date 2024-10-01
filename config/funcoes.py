#from bs4 import BeautifulSoup
import requests
#from selenium import webdriver
from time import sleep
import bd as ac
import api_sports as asp
from datetime import datetime
import asyncio
import mensageiro
from time import sleep

#api_sports

def league_treatment():

    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    leagues = asp.search_leagues()
    
    leagues = leagues["response"]

    for league in leagues:
        dic_league = league["league"]
        id_league = dic_league["id"]
        name_league = dic_league["name"]
        tipy_league = dic_league["type"]
        logo_league = dic_league["logo"]

        dic_country = league["country"]
        name_country = dic_country["name"]
        code_country = dic_country["code"]
        flag_country = dic_country["flag"]
        
        ac.insert_country(conn,cursor,name_country,code_country,flag_country)
        ac.insert_league(conn,cursor,id_league,name_league,tipy_league,logo_league,name_country)
    
    ac.close_connection(conn,cursor)

    return

def teams_stadium_treatment():

    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    leagues = ac.search_leagues_team(cursor)

    for league in leagues:

        teams_stadium = asp.teams_leagues(league[0],2024)
        
        teams_stadium = teams_stadium["response"]

        for i in teams_stadium:

            team = i["team"]

            id_team = team["id"]
            name_team = team["name"]
            code_team = team["code"]
            country = team["country"]
            founded_team = team["founded"]
            national_team = team["national"]
            logo_team = team["logo"]

            ac.insert_team(conn,cursor,id_team, name_team, code_team,country,founded_team,national_team,logo_team)

            stadium = i["venue"]

            id_stadium = stadium["id"]
            name_stadium = stadium["name"]
            address_stadium = stadium["address"]
            city_stadium = stadium["city"]
            capacity_stadium = stadium["capacity"]
            surface_stadium = stadium["surface"]
            image_stadium = stadium["image"]

            ac.insert_stadium(conn,cursor,id_stadium, name_stadium, address_stadium, city_stadium, country, capacity_stadium, surface_stadium, image_stadium,id_team)

    ac.close_connection(conn,cursor)

    return

def treatment_table():
    
    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    leagues = ac.search_leagues(cursor)

    for league in leagues:

        table = asp.league_table(league[0],2024)

        response = table["response"][0]

        league_response = response["league"]

        id_league = league_response["id"]
        season = league_response["season"]

        standings = league_response["standings"][0]

        for rank in standings:
            rank_team = rank["rank"]
            team = rank["team"]
            id_team = team["id"]
            points = rank["points"]
            goalsDiff = rank["goalsDiff"]
            form = rank["form"]
            status = rank["status"]
            description = rank["description"]
            all = rank["all"]
            played = all["played"]
            win = all["win"]
            draw = all["draw"]
            lose = all["lose"]
            goals = all["goals"]
            gf = goals["for"]
            ga = goals["against"]

            ac.insert_table(conn,cursor,id_league,rank_team,id_team,points,goalsDiff,form,status,description,played,win,draw,lose,gf,ga,season)

    ac.close_connection(conn,cursor)

    return

def game_of_the_day():

    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    leagues = ac.search_leagues(cursor)

    data_formatada = datetime.now().strftime("%Y-%m-%d")

    for league in leagues:
        
        sleep(3)
        game_day = asp.play_date(data_formatada,league[0],2024)

        response = game_day["response"]

        if len(response) == 0:
            sleep(3)
            pass
        
        else:
            for game in response:
                fixture = game["fixture"]
                id_game = fixture["id"]
                date = fixture["date"]
                venue = fixture["venue"]
                id_venue = venue["id"]
                league_game = game["league"]
                id_league = league_game["id"]
                season = league_game["season"]
                round = league_game["round"]
                teams = game["teams"]
                home = teams["home"]
                id_team_home = home["id"]
                away = teams["away"]
                id_team_away = away["id"]
                goals = game["goals"]
                goals_home = goals["home"]
                goals_away = goals["away"]

                ac.insert_game(conn,cursor,id_game,date,id_venue,id_league,season,round,id_team_home,id_team_away,goals_home,goals_away)
                sleep(3)

    ac.close_connection(conn,cursor)

    return

def game_of_the_day_cup():

    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    leagues = ac.search_cup(cursor)

    data_formatada = datetime.now().strftime("%Y-%m-%d")

    for league in leagues:
        
        sleep(3)
        game_day = asp.play_date(data_formatada,league[0],2024)

        response = game_day["response"]

        if len(response) == 0:
            sleep(3)
            pass
        
        else:
            for game in response:
                fixture = game["fixture"]
                id_game = fixture["id"]
                date = fixture["date"]
                venue = fixture["venue"]
                id_venue = venue["id"]
                league_game = game["league"]
                id_league = league_game["id"]
                season = league_game["season"]
                round = league_game["round"]
                teams = game["teams"]
                home = teams["home"]
                id_team_home = home["id"]
                away = teams["away"]
                id_team_away = away["id"]
                goals = game["goals"]
                goals_home = goals["home"]
                goals_away = goals["away"]

                ac.insert_game(conn,cursor,id_game,date,id_venue,id_league,season,round,id_team_home,id_team_away,goals_home,goals_away)
                sleep(3)

    ac.close_connection(conn,cursor)

    return

def predictions():

    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    games = ac.search_for_games_of_the_day(cursor)
    
    for game in games:

        prediction = asp.predictions(game[0])

        try:
            response = prediction['response'][0]

            prediction_result = response["predictions"]
            winner = prediction_result["winner"]
            winner_id = winner['id']
            winner_comment = winner['comment']
            win_or_draw = prediction_result["win_or_draw"]
            under_over = prediction_result["under_over"]
            goals = prediction_result["goals"]
            goals_home = goals["home"]
            goals_away = goals["away"]
            advice = prediction_result["advice"]
            percent = prediction_result["percent"]
            percent_home = percent["home"]
            percent_draw = percent["draw"]
            percent_away = percent["away"]

            league = response["league"]
            id_league = league["id"]
            
            message = f"""O jogo {game[1]} X {game[2]}\n Horario {game[3]}:\n\n (comentário: {winner_comment}). Projeção de gols: Casa: {goals_home}. Visitante: {goals_away}. Recomendação: {advice}."""
                        
            loop = asyncio.get_event_loop()
            loop.run_until_complete(mensageiro.enviar_mensagem(message))

            ac.inset_predictions(conn,cursor,game[0],winner_id,winner_comment,win_or_draw,under_over,goals_home,goals_away,advice,percent_home,percent_draw,percent_away,id_league)
            sleep(3)

        except:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(mensageiro.enviar_mensagem(f'Deu erro na previsão do jogo: {game[0]}'))
            sleep(3)

    ac.close_connection(conn,cursor)

    return

def run():

    with open("config/Tabela.txt", "r") as arquivo:
        resultado = arquivo.read()
    
    if resultado == 'N': #configuração incial
        ac.create_table()
        league_treatment()
        teams_stadium_treatment()
        treatment_table()
        game_of_the_day()
        game_of_the_day_cup()
        predictions()
    
    else: #Atualização_normal 
        treatment_table()
        game_of_the_day()
        game_of_the_day_cup()
        predictions()

    return