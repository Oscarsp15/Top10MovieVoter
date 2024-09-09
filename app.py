import os
import requests
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv

# Load the .env file with the API key
load_dotenv()

app = Flask(__name__)

# Set TMDB API URL and your API Key
BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = os.getenv('TMDB_API_KEY')

# Fetch movies data from TMDB API
def get_movies():
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    return response.json().get('results', [])

# Fetch movie details by ID from TMDB API
def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    # Get popular movies and sort them based on vote count
    movies = get_movies()
    sorted_movies = sorted(movies, key=lambda x: x['vote_count'], reverse=True)
    return render_template('index.html', movies=sorted_movies)

@app.route('/search')
def search():
    query = request.args.get('movie')
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&language=es-ES&query={query}"
    response = requests.get(url)
    result = response.json().get('results', [])
    return render_template('index.html', movies=result)

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    # Fetch detailed movie information
    movie = get_movie_details(movie_id)
    genre_names = ', '.join([genre['name'] for genre in movie['genres']])
    return render_template('movie_details.html', movie=movie, genre_names=genre_names)

@app.route('/vote', methods=['POST'])
def vote():
    # Votes handling (this should be linked to a database for persistence)
    movie_id = int(request.form['movie_id'])
    movie = get_movie_details(movie_id)
    # Assuming we're simulating vote count here; you can store votes in a DB for real scenarios
    movie['vote_count'] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run()
