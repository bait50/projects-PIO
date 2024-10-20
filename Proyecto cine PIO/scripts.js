const peliculas = [
    {
        nombre: "JOKER 2: FOLIE à DEUX",
        genero: "Drama, Musical",
        duracion: "2h 15min",
        calificacion: "8.5/10",
        horarios: "15:00, 18:00, 21:00"
    },
    {
        nombre: "Deadpool & Wolverine",
        genero: "Acción, Comedia",
        duracion: "1h 58min",
        calificacion: "9.0/10",
        horarios: "15:00, 18:00, 21:00"
    },
    {
        nombre: "Beetlejuice 2",
        genero: "Comedia, Fantasía",
        duracion: "1h 45min",
        calificacion: "7.8/10",
        horarios: "15:00, 18:00, 21:00"
    },
    {
        nombre: "EL reino animal",
        genero: "Drama, Aventura",
        duracion: "2h 10min",
        calificacion: "8.0/10",
        horarios: "15:00, 18:00, 21:00"
    },
    {
        nombre: "El juego del año",
        genero: "Suspenso, Thriller",
        duracion: "1h 50min",
        calificacion: "7.5/10",
        horarios: "15:00, 18:00, 21:00"
    },
    {
        nombre: "El hombre de las montañas",
        genero: "Aventura, Biografía",
        duracion: "2h 20min",
        calificacion: "7.9/10",
        horarios: "15:00, 18:00, 21:00"
    }
];

// Función para redirigir a la página de reserva
function redirigirAReserva(peliculaNombre) {
    const pelicula = peliculas.find(p => p.nombre === peliculaNombre);
    if (pelicula) {
        localStorage.setItem("peliculaSeleccionada", JSON.stringify(pelicula));
        window.location.href = "reserva.html";
    }
}

// Al cargar la página de reserva, mostrar los detalles de la película seleccionada
document.addEventListener("DOMContentLoaded", function () {
    const peliculaData = JSON.parse(localStorage.getItem("peliculaSeleccionada"));
    if (peliculaData) {
        document.getElementById("pelicula").value = peliculaData.nombre;
        document.getElementById("genero").textContent = `Género: ${peliculaData.genero}`;
        document.getElementById("duracion").textContent = `Duración: ${peliculaData.duracion}`;
        document.getElementById("calificacion").textContent = `Calificación: ${peliculaData.calificacion}`;
        document.getElementById("horarios").textContent = `Horarios: ${peliculaData.horarios}`;
    }
});




