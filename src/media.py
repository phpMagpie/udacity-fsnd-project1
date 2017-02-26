import webbrowser
import urllib
import json


class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Initiates the Movie instance and sets it's variables"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """DEPRECATED: Javascript that fresh_tomatoes.py outputs now
        handles trailer loading.

        Opens a new browser window/tab using the trailer_youtube_url"""

        webbrowser.open(self.trailer_youtube_url)
        
        
class MovieTMDb():
    def __init__(self, id):
        """Initiates the Movie instance and sets it's variables"""
        
        api_key = "1ae3d866347edd31cc255beccd4cb107"
        
        # Fetch movie details from TMDb
        movie_request = urllib.urlopen("https://api.themoviedb.org/3/movie/" + str(id) + "?api_key=" + api_key)
        movie_result = movie_request.read()
        movie_result = json.loads(movie_result)
        movie_request.close()
        
        # Fetch movies videos from TMDb
        video_request = urllib.urlopen("https://api.themoviedb.org/3/movie/" + str(id) + "/videos?language=en-US&api_key=" + api_key)
        video_result = video_request.read()
        video_result = json.loads(video_result)
        video_request.close()
        
        # Set instance variables
        self.title = movie_result["title"]
        self.storyline = movie_result["tagline"]
        self.poster_image_url = "https://image.tmdb.org/t/p/w640" + movie_result["poster_path"]
        self.trailer_youtube_url = video_result["results"][0]["key"]
