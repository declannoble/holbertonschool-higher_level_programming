$.get('https://swapi-api.hbtn.io/api/people/5/?format=json' ,function (response){
    $('#character').html(response.name)
}
    )