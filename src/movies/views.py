from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from movies.modules.loadMoviesOnStart import *

def index(request):
    ia = IMDb('http')
    response = []
    if request.is_ajax():
        query = request.POST
        if int(query['requestType']) == 0:
            movieQuery = ia.search_movie(str(query['movieTitle']))
            i = 0
            while len(movieQuery) >= 3 and i <= 3:
                response.append({
                    'title' : movieQuery[i].get('title'),
                    'cover' : modUrl(movieQuery[i].get('cover'))
                })
                i+=1
            return HttpResponse(json.dumps(response))
        else:
            return HttpResponse(404)
    else:
        context = getTop()
        return render(request, 'index.html', {'context': context})

def result(request, movieTitle):
    ia = IMDb('http')
    movieQuery = ia.search_movie(movieTitle)[0]
    print(ia.get_movie_infoset())
    ia.update(movieQuery, ['release'])
    #work checkpoint/stop here
    context = {
        'title': movieQuery.get('title'),
        'cover': modUrl(movieQuery['cover url']),
        'release': movieQuery.get('release info'),
        'awards': movieQuery.get('awards'),
        'credits': movieQuery.get('full credits'),
        'keywords': movieQuery.get('keywords'),
        'plot': movieQuery.get('plot'),
        'news': movieQuery.get('news'),
        'sites': movieQuery.get('official sites'),
        'video': movieQuery.get('video clips'),
        'rating': movieQuery.get('vote details')
    }
    return render(request, 'result.html', context=context)
