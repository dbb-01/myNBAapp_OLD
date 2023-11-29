

// Solicitud AJAX para obtener estadísticas de equipos
document.addEventListener('DOMContentLoaded', function () {
    const resultadoDiv = document.getElementById('players');

    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5000/player/1610612741', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);

            // Limpia el div
            resultadoDiv.innerHTML = '';

            data.forEach((jugador) => {
                
                const filaEquipo = document.createElement('tr');
                filaEquipo.innerHTML = `
                    <td>${jugador.PLAYER}</td>
                    <td>${jugador.AGE}</td>
                    <td>${jugador.HEIGHT}</td>
                    <td>${jugador.WEIGHT}</td>
                    <td>${jugador.POSITION}</td>
                    <td>${jugador.EXP}</td>

                    
                `;

                resultadoDiv.appendChild(filaEquipo);
            });
            
        } else {
            console.error('Error al cargar el JSON.');
        }
    };

    xhr.send();
});

// En tu script JavaScript
document.getElementById('bulls').addEventListener('click',buscar)

    function buscar(){
    const resultadoDiv = document.getElementById('r');
    const valor = document.getElementById("bulls").dataset.valor;

    const name = valor;
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `http://127.0.0.1:5000/getTeamIdbyName/${name}`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);

            const idEquipo = data.team_id;

            resultadoDiv.innerHTML = `El ID del equipo es: ${idEquipo}`;
        } else {
            console.error('Error al cargar el JSON.');
        }
    };

    xhr.send();
};
