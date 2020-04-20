from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from imdb import IMDb
import json

# dziwny bug z rozłączającym się socketem
# nie wpływa na działanie strony.

def index(request):
    ia = IMDb('http')
    response = {}
    if request.is_ajax():
        query = request.POST
        if int(query['requestType']) == 0:
            movieQuery = ia.search_movie(str(query['movieTitle']))
            i = 0
            while len(movieQuery) >= 3 and i <= 3:
                response[i] = {
                    'title' : movieQuery[i].get('title'),
                    'cover' : movieQuery[i].get('cover')
                }
                i+=1
            return HttpResponse(json.dumps(response))
        else:
            return HttpResponse(404)
    else:
        return render(request, 'index.html')

def result(request, movieTitle):
    ia = IMDb('http')
    movieQuery = ia.search_movie(movieTitle)[0]
    print(movieQuery)
    context = {
        'title': movieQuery.get('title'),
        # Przerobić linki z gorszej rozdzielczości na lepszą.
        # https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg
        # https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,32,44_AL_.jpg
        'cover': movieQuery['cover url']
    }
    return render(request, 'result.html', context=context)
