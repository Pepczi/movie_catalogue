import requests
import pprint

pp = pprint.PrettyPrinter()

def get_json(url_api):
    #url = "https://api.themoviedb.org/3/movie/popular"
    url = url_api
    headers = {'Authorization' : "Bearer "}
    respone = requests.get(url,headers=headers)
    return respone.json()

def configuration_json():
    url = "https://api.themoviedb.org/3/configuration"
    headers = {'Authorization' : "Bearer "}
    configuration = requests.get(url,headers=headers)
    return configuration.json()

def get_movie_id(url_api):
    data = get_json(url_api)
    id = ['results']['id']


def get_movie_details(id):
    url_for_id =  f"{'https://api.themoviedb.org/3/movie/'}{id}"
    data = get_json(url_for_id)
    return data


def poster_url(url_api,size='w342'):
    configuartion = configuration_json()
    movie_info = get_json(url_api)
    base_url = f"{configuartion['images']['base_url']}{size}"
    posters_url_list = []
    for info in movie_info['results']:
        posters_url_list.append(f"{base_url}{info['poster_path']}")
    return posters_url_list

def title_posters_list(url_api, size='w342'):
    movie_info = get_json(url_api)
    url_poster = poster_url(url_api, size)
    title_poster = []
    for info in movie_info['results']:
        title_poster.append(f"{info['title']}")
    posters_url_list = []
    for i, k in zip(title_poster, url_poster):
        posters_url_list.append({i : k})
    return posters_url_list





