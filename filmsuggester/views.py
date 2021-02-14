from django.http import HttpResponse
from django.http import JsonResponse

def message(request):
    return HttpResponse("Hello, world!")

mock_films_data = {
    "results": [
        { "title": "The Shawshank Redemption", "description": "Pretty decent film bout a guy in prison", "image": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg" },
        { "title": "The Godfather", "description": "some italian old chap get's pretty spicy", "image": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg"},
        { "title": "The Dark Knight", "description": "adult man dresses in bat costume and lowers his voice", "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg" },
        { "title": "12 Angry Men", "description": "old film about jurors, actually better than it sounds", "image": "https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX182_CR0,0,182,268_AL_.jpg"}
    ]
}

def films(request):
    return JsonResponse(mock_films_data)
