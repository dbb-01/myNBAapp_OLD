from flask import Flask, jsonify
from flask_cors import CORS
from nba_api.stats.endpoints import leaguestandings
from nba_api.stats.endpoints import leagueleaders
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams


from pandas import DataFrame
import json



#ID TEAMS
ciudad = teams.find_teams_by_city('Boston')
df=  ciudad[0]
id = df['id']
print(id)

