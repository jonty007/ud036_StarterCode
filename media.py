#!/usr/bin/env python
"""Movie class defination."""

import webbrowser

class Movie(object):
    """Class Movie to store movie details and show trailer
    Attributes:
        movie_title: Title of the movie.
        movie_storyline: Storyline of the movie.
        poster_image: URL to the poster of the movie.
        trailer_youtube: URL to the trailer of the movie.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Show trailer of the movie."""
        webbrowser.open(self.trailer_youtube_url)
