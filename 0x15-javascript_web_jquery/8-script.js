$.get('https://swapi-api.hbtn.io/api/films/?format=json' ,function (response){
    let movies = response.results;
    for (let i in movies) {
        $('#list_movies').append('<li>'+ movies[i].title + '</li>')
    }
})