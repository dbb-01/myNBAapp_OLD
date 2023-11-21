

// Solicitud AJAX para obtener estadísticas de equipos
document.addEventListener('DOMContentLoaded', function () {
    const resultadoDiv = document.getElementById('equipos');

    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5000/obtener_estadisticas_equipos', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);

            // Limpia el div
            resultadoDiv.innerHTML = '';

            data.forEach((equipo, index) => {
                const nombreEquipo = equipo.TEAM_NAME;
                const victorias = equipo.W;
                const derrotas = equipo.L;
                const porcentajeVictorias = equipo.W_PCT;
                const rebotes = equipo.REB;
                const asistencias = equipo.AST;
                const perdidas = equipo.TOV;
                const puntos = equipo.PTS;

                const filaEquipo = document.createElement('tr');
                filaEquipo.innerHTML = `
                    <th scope="row">${index + 1}</th>
                    <td>${nombreEquipo}</td>
                    <td>${victorias}</td>
                    <td>${derrotas}</td>
                    <td>${porcentajeVictorias}</td>
                    <td>${rebotes}</td>
                    <td>${asistencias}</td>
                    <td>${perdidas}</td>
                    <td>${puntos}</td>
                `;

                resultadoDiv.appendChild(filaEquipo);
            });
        } else {
            console.error('Error al cargar el JSON.');
        }
    };

    xhr.send();
});
