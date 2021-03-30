from flask import Flask, render_template, request, url_for, redirect, flash
import datetime
from tmdb_client import tmdb

app = Flask(__name__)
FAVORITES = set()
app.secret_key = b'tak'

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    print(selected_list)
    movies = tmdb.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb.get_single_movie(movie_id)
    cast = tmdb.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)

@app.route('/search')
def search():
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb.search_movie(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)

@app.route('/today')
def today():
    movies = tmdb.playing_today()
    today = datetime.date.today()
    return render_template("today.html", movies=movies, today=today)

@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id and movie_title:
        FAVORITES.add(movie_id)
        flash(f'Dodano film {movie_title} do ulubionych!')
    return redirect(url_for('homepage'))

@app.route("/favorites")
def show_favorites():
    if FAVORITES:
        movies = []
        for movie_id in FAVORITES:
            movie_details = tmdb.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template("homepage.html", movies=movies)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb.get_poster_movie(path, size)
    return {"tmdb_image_url": tmdb_image_url}

if __name__ == '__main__':
    app.run(debug=True)