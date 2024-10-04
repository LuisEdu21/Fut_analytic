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
import traceback

#api_sports

def treatment_season():
    
    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    seasons = asp.nba_seasons()

    for seasson in seasons["response"]:
        ac.insert_seasons_nba(conn,cursor,seasson)

    return

def treatment_league():
    
    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    leagues = asp.nba_leagues()

    for league in leagues["response"]:
        ac.insert_leagues_nba(conn,cursor,league)

    return

def treatment_games_seasons():

    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    seasons = ac.search_seasons_nba(cursor)


    for season in seasons:

        games = asp.nba_games(season[0])

        for game in games["response"]:
            id_game = game["id"]
            league = game["league"]
            season = game["season"]
            
            dates = game["date"]
            start = dates["start"]
            end = dates["end"]
            duration = dates["duration"]
            stage = game["stage"]
            
            status = game["status"]
            clock = status["clock"]
            halftime = status["halftime"]
            short = status["short"]
            long = status["long"]

            periods = game["periods"]
            current = periods["current"]
            total = periods["total"]
            endOfPeriod = periods["endOfPeriod"]

            arena = game["arena"]
            name = arena["name"]
            city = arena["city"]
            state = arena["state"]
            country = arena["country"]

            teams = game["teams"]
            team_visitors = teams["visitors"]
            id_visitors = team_visitors["id"]

            team_home = teams["home"]
            id_home = team_home["id"]

            scores = game["scores"]
            scores_visitors = scores["visitors"]
            scores_visitors_win = scores_visitors["win"]
            scores_visitors_loss = scores_visitors["loss"]

            scores_visitors_series = scores_visitors["series"]
            scores_visitors_series_win = scores_visitors_series["win"]
            scores_visitors_series_loss = scores_visitors_series["loss"]

            scores_visitors_linescore = scores_visitors["linescore"]

            scores_visitors_points = scores_visitors["points"]

            scores_home = scores["home"]
            scores_home_win = scores_home["win"]
            scores_home_loss = scores_home["loss"]

            scores_home_series = scores_home["series"]
            scores_home_series_win = scores_home_series["win"]
            scores_home_series_loss = scores_home_series["loss"]

            scores_home_linescore = scores_home["linescore"]

            scores_home_points = scores_home["points"]

            ac.insert_game_nba(conn,cursor,id_game, league, season, start, end, duration, stage, clock, halftime, short, long, current, total, endOfPeriod, name, city, state, country, id_visitors, id_home, scores_visitors_points, scores_home_points)

    return

def treatment_games():

    conn = ac.connection_with_bank()

    cursor = conn.cursor()

    data_formatada = datetime.now().strftime("%Y-%m-%d")

    games = asp.nba_games(data_formatada)

    for game in games["response"]:
        id_game = game["id"]
        league = game["league"]
        season = game["season"]
        
        dates = game["date"]
        start = dates["start"]
        end = dates["end"]
        duration = dates["duration"]
        stage = game["stage"]
        
        status = game["status"]
        clock = status["clock"]
        halftime = status["halftime"]
        short = status["short"]
        long = status["long"]

        periods = game["periods"]
        current = periods["current"]
        total = periods["total"]
        endOfPeriod = periods["endOfPeriod"]

        arena = game["arena"]
        name = arena["name"]
        city = arena["city"]
        state = arena["state"]
        country = arena["country"]

        teams = game["teams"]
        team_visitors = teams["visitors"]
        id_visitors = team_visitors["id"]

        team_home = teams["home"]
        id_home = team_home["id"]

        scores = game["scores"]
        scores_visitors = scores["visitors"]
        scores_visitors_win = scores_visitors["win"]
        scores_visitors_loss = scores_visitors["loss"]

        scores_visitors_series = scores_visitors["series"]
        scores_visitors_series_win = scores_visitors_series["win"]
        scores_visitors_series_loss = scores_visitors_series["loss"]

        scores_visitors_linescore = scores_visitors["linescore"]

        scores_visitors_points = scores_visitors["points"]

        scores_home = scores["home"]
        scores_home_win = scores_home["win"]
        scores_home_loss = scores_home["loss"]

        scores_home_series = scores_home["series"]
        scores_home_series_win = scores_home_series["win"]
        scores_home_series_loss = scores_home_series["loss"]

        scores_home_linescore = scores_home["linescore"]

        scores_home_points = scores_home["points"]

        ac.insert_game_nba(conn,cursor,id_game, league, season, start, end, duration, stage, clock, halftime, short, long, current, total, endOfPeriod, name, city, state, country, id_visitors, id_home, scores_visitors_points, scores_home_points)


    return


treatment_games_seasons()