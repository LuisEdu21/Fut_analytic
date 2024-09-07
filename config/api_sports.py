import requests
import os
from dotenv import load_dotenv

load_dotenv()

def search_leagues():

  url = "https://v3.football.api-sports.io/leagues"

  payload = {}
  headers = {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': os.getenv('token_api_sports')
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

  return response.json()

def teams_leagues(league,season):

  url = f"https://v3.football.api-sports.io/teams?league={league}&season={season}"

  payload = {}
  headers = {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': os.getenv('token_api_sports')
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

  return response.json()
