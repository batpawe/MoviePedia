from imdb import IMDb
from random import randrange

def modUrl(txt):
    return txt.split('@', 1)[0] + '@.jpg'


context = {}
ia = IMDb('http')
i = 0
while i <= 4:
    movieQuery = ia.get_top250_movies()
    movieId = randrange(0,249)
    image_url = modUrl(ia.search_movie(movieQuery[movieId].get('title'))[0]['cover'])
    if image_url != None:
        context[i] = {
            'title' : movieQuery[movieId]['title'],
            'cover' : image_url
        }
        i+=1

def getTop():
    return context
