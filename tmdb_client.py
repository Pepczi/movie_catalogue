import requests

API_TOKEN = ""

class Movie_data():
    def __init__(self):
        self.headers = {'Authorization' : f"Bearer {API_TOKEN}"}

    def get_configuration(self):
        config = "https://api.themoviedb.org/3/configuration"
        configuration = requests.get(config, headers=self.headers)
        return configuration.json()

    def get_movie_info(self, url_api):
        respone = requests.get(url_api, headers=self.headers)
        return respone['results'].json()
    
    def get_id(self, url_api):
        data = self.get_movie_info()
        return data['results']['id']

    def get_popular_movies(self, list_type='popular'):
        endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def get_poster_movie(self, poster_path, size='w342'):
        base_url = "https://image.tmdb.org/t/p/"
        return f"{base_url}{size}{poster_path}"

    def get_movies(self, how_many, list_type='popular'):
        data = self.get_popular_movies(list_type)
        return data["results"][:how_many]

    def get_single_movie(self, movie_id):
        endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def get_single_movie_cast(self, movie_id):
        endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def get_movies_list(self, list_type):
        endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_movie(self, search_query):
        endpoint = f"https://api.themoviedb.org/3/search/movie?query={search_query}"
        response = requests.get(endpoint, headers=self.headers)
        response = response.json()
        return response['results']

    def playing_today(self):
        endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
        response = requests.get(endpoint, headers=self.headers)
        response = response.json()
        return response['results']



tmdb = Movie_data()


