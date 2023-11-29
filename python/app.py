from flask import Flask, jsonify, request
from flask_cors import CORS
from nba_api.stats.endpoints import leaguestandings
from nba_api.stats.endpoints import leagueleaders
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
 



from pandas import DataFrame
import json

app = Flask(__name__)

CORS(app)


#Clasificación ESTE
@app.route('/obtener_clasificacion_este', methods=['GET'])
def obtener_clasificacion_este():
    standings = leaguestandings.LeagueStandings(season='2023-24')
    data_frame = standings.get_data_frames()[0]
    equipos_conferencia_este = data_frame[data_frame['Conference'] == 'East']

    equipos_lista = []

    for index, equipo in equipos_conferencia_este.iterrows():
        nombre_ciudad = equipo['TeamCity']
        nombre_equipo = equipo['TeamName']
        record = f"{equipo['WINS']}-{equipo['LOSSES']}"

        equipo_dict = {
            'nombre_ciudad': nombre_ciudad,
            'nombre_equipo': nombre_equipo,
            'record': record
        }

        equipos_lista.append(equipo_dict)

    return jsonify(equipos_lista)

#Clasificación OESTE
@app.route('/obtener_clasificacion_oeste', methods=['GET'])
def obtener_clasificacion_oeste():
    standings = leaguestandings.LeagueStandings(season='2023-24')
    data_frame = standings.get_data_frames()[0]
    equipos_conferencia_este = data_frame[data_frame['Conference'] == 'West']

    equipos_lista = []

    for index, equipo in equipos_conferencia_este.iterrows():
        nombre_ciudad = equipo['TeamCity']
        nombre_equipo = equipo['TeamName']
        record = f"{equipo['WINS']}-{equipo['LOSSES']}"

        equipo_dict = {
            'nombre_ciudad': nombre_ciudad,
            'nombre_equipo': nombre_equipo,
            'record': record
        }

        equipos_lista.append(equipo_dict)

    return jsonify(equipos_lista)


#Clasificación Max_anotadores
@app.route('/max_anotadores', methods=['GET'])
def max_anotadores():
     # máximos anotadores de la liga por partido
    leaders = leagueleaders.LeagueLeaders(per_mode48='PerGame')

    # formato DataFrame
    data_frame = leaders.get_data_frames()[0]

    # Filtrar dataframe 
    data_frame_filtered = data_frame[['PLAYER', 'PTS']]

    # Ordenar
    data_frame_filtered = data_frame_filtered.sort_values(by='PTS', ascending=False)

    # 10 primeros
    top_10_jugadores = data_frame_filtered.head(10)

    # Convertir datos a diccionario
    top_10_jugadores_dict = top_10_jugadores.to_dict(orient='records')

    # Devolver el resultado
    return jsonify(top_10_jugadores_dict)

#Clasificación Max_reboteadores
@app.route('/max_reboteadores', methods=['GET'])
def max_reboteadores():
     # máximos reboteadores de la liga por partido
    leaders = leagueleaders.LeagueLeaders(per_mode48='PerGame')

    # formato DataFrame
    data_frame = leaders.get_data_frames()[0]

    # Filtrar dataframe 
    data_frame_filtered = data_frame[['PLAYER', 'REB']]

    # Ordenar
    data_frame_filtered = data_frame_filtered.sort_values(by='REB', ascending=False)

    # 10 primeros
    top_10_jugadores = data_frame_filtered.head(10)

    # Convertir datos a diccionario
    top_10_jugadores_dict = top_10_jugadores.to_dict(orient='records')

    # Devolver el resultado
    return jsonify(top_10_jugadores_dict)

#Clasificación Max_anotadores
@app.route('/max_asistentes', methods=['GET'])
def max_asistentes():
     # máximos asistentes de la liga por partido
    leaders = leagueleaders.LeagueLeaders(per_mode48='PerGame')

    # formato DataFrame
    data_frame = leaders.get_data_frames()[0]

    # Filtrar dataframe 
    data_frame_filtered = data_frame[['PLAYER', 'AST']]

    # Ordenar
    data_frame_filtered = data_frame_filtered.sort_values(by='AST', ascending=False)

    # 10 primeros
    top_10_jugadores = data_frame_filtered.head(10)

    # Convertir datos a diccionario
    top_10_jugadores_dict = top_10_jugadores.to_dict(orient='records')

    # Devolver el resultado
    return jsonify(top_10_jugadores_dict)


#stats_equipos
@app.route('/player/<team>', methods=['GET'])
def player(team):
    
    players = commonteamroster.CommonTeamRoster(team_id=getTeam(str(team)), season ='2023-24')
    playersdf = players.get_data_frames()[0]


    # Filtrar dataframe 
    data_frame_filtered = playersdf[[
        'PLAYER',
        'POSITION',
        'AGE',
        'HEIGHT',
        'WEIGHT',
        'POSITION',
        'EXP',
        'TeamID'
        ]]


    # Convertir datos a diccionario
    data_frame_filtered_dict = data_frame_filtered.to_dict(orient='records')

    # Devolver el resultado
    return jsonify(data_frame_filtered_dict)

    

#stats_equipos
@app.route('/obtener_estadisticas_equipos', methods=['GET'])
def obtener_estadisticas_equipos():
    
    standings = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='PerGame')
    equipos = standings.get_data_frames()[0]

    equipos_lista = []

    for index, equipo in equipos.iterrows():
        nombre_equipo = equipo['TEAM_NAME']
        record = f"{equipo['W']}-{equipo['L']}"
        ppp = equipo['PTS']
        rpp = equipo['REB']
        app = equipo['AST']
        fg = equipo['FG_PCT']
        fg3 = equipo['FG3_PCT']
        stl = equipo['STL']
        blk = equipo['BLK']
        w_pct = equipo['W_PCT']

        equipo_dict = {
            'nombre_equipo': nombre_equipo,
            'record': record,
            'ppp' : ppp,
            'rpp' : rpp,
            'app' : app,
            'fg' : fg,
            'fg3' : fg3,
            'stl' : stl,
            'blk' : blk,
            'w_pct' : w_pct

        }

        equipos_lista.append(equipo_dict)

    return jsonify(equipos_lista)

#ID TEAMS
@app.route('/getTeamIdbyName/<name>', methods=['GET'])
def getTeamIdbyName(name):
    ciudad = teams.find_teams_by_city(str(name))
    df = ciudad[0]
    team_id = df['id']
    return jsonify({'team_id': team_id})

def getTeam(name):
    ciudad = teams.find_teams_by_city(str(name))
    df = ciudad[0]
    team_id = df['id']
    return jsonify({'team_id': team_id})
#FINAL
if __name__ == '__main__':
    app.run(debug=True)