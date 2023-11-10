document.addEventListener('DOMContentLoaded', function () {
    const resultadoDiv = document.getElementById('clas_este');

    // Solicitud AJAX para clasificación ESTE
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5000/obtener_clasificacion_este', true);  // Reemplaza con la URL de tu servidor Flask
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);

            // Limpia el div
            resultadoDiv.innerHTML = '';

            // Itera a través de los equipos y escribe en el div
            data.forEach(equipo => {
                const nombreCiudad = equipo.nombre_ciudad;
                const nombreEquipo = equipo.nombre_equipo;
                const record = equipo.record;

                const equipoInfo = document.createElement('p');
                equipoInfo.textContent = `${nombreCiudad} ${nombreEquipo} - ${record}`;
                resultadoDiv.appendChild(equipoInfo);
            });
        } else {
            console.error('Error al cargar el JSON.');
        }
    };

    xhr.send();
});


document.addEventListener('DOMContentLoaded', function () {
    const resultadoDiv = document.getElementById('clas_oeste');

    // Solicitud AJAX para clasificación OSTE
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5000/obtener_clasificacion_oeste', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
        if (xhr.status === 200) {
            const data = JSON.parse(xhr.responseText);

            // Limpia el div
            resultadoDiv.innerHTML = '';

            // Itera a través de los equipos y escribe en el div
            data.forEach(equipo => {
                const nombreCiudad = equipo.nombre_ciudad;
                const nombreEquipo = equipo.nombre_equipo;
                const record = equipo.record;

                const equipoInfo = document.createElement('p');
                equipoInfo.textContent = `${nombreCiudad} ${nombreEquipo} - ${record}`;
                resultadoDiv.appendChild(equipoInfo);
            });
        } else {
            console.error('Error al cargar el JSON.');
        }
    };

    xhr.send();
});