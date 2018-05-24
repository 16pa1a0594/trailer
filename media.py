#!/usr/bin/env python
import webbrowser


class Movie():
    """Class describing attributes and behaviour of movie.
Args:
     movie_titile: title of movie.
     poster_image: decribes about image.
     trailer_youtube: discuss about trailer link.
Methods:
     show_trailer(str): prints message from class movie."""
    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

