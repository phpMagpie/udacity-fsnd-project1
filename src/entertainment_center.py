import fresh_tomatoes
import media

# Fetch movies from TMDb API
movie1 = media.MovieTMDb(11)
movie2 = media.MovieTMDb(9476)
movie3 = media.MovieTMDb(10719)
movie4 = media.MovieTMDb(14160)
movie5 = media.MovieTMDb(583)
movie6 = media.MovieTMDb(941)

# Add movies into a list
movies = [movie1, movie2, movie3, movie4, movie5, movie6]

# Generate and open HTML file using list of movies
fresh_tomatoes.open_movies_page(movies)
