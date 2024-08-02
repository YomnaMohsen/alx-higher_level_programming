$(document).ready(function() {
    $.get( "https://swapi-api.alx-tools.com/api/films/?format=json", (data) => {
        $.each(data.results, function(i, film){
            $("#list_movies").append('<li>' + film.title + '</li>')
        });
    });
  });

