from flask import Flask, jsonify
from flask_cors import CORS
from nba_api.stats.endpoints import leaguestandings
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

if __name__ == '__main__':
    app.run(debug=True)