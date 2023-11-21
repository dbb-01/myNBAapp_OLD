from flask import Flask, jsonify
from flask_cors import CORS
from nba_api.stats.endpoints import leaguestandings
from nba_api.stats.endpoints import leagueleaders
from nba_api.stats.endpoints import leaguedashteamstats

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
@app.route('/obtener_estadisticas_equipos', methods=['GET'])
def obtener_estadisticas_equipos():
    
    standings = leaguedashteamstats.LeagueDashTeamStats()
    data_frame = standings.get_data_frames()[0]
    equipos= data_frame[0]

    equipos_lista = []

    for index, equipo in equipos.iterrows():
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

#FINAL
if __name__ == '__main__':
    app.run(debug=True)