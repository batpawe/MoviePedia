from imdb import IMDb
from random import randrange

def modUrl(txt):
    return txt.split('@', 1)[0] + '@'


context = {}
ia = IMDb('http')
i = 0
while i <= 4:
    movieQuery = ia.get_top250_movies()
    image_url = modUrl(ia.search_movie(movieQuery[i].get('title'))[0]['cover'])
    if i == 3:
        image_url = image_url + '@'

    if image_url != None:
        context[i] = {
            'title' : movieQuery[i]['title'],
            'cover' : image_url
        }
    i+=1

def getTop():
    return context
