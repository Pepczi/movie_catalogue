from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)



@app.route('/')
def homepage(url_movie = "https://api.themoviedb.org/3/movie/popular"):
    movies = tmdb_client.get_json(url_movie)
    movie_id = tmdb_client.get_movie_id(url_movie)
    return render_template("homepage.html", movies=movies, movie_id=movie_id)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_movie_details(movie_id)
    return render_template("movie_details.html", movie=details)


if __name__ == '__main__':
    app.run(debug=True)