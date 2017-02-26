import webbrowser


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
