import webbrowser


class Movie():
    """
            This is the movie class. In order the store information of movies,
            instances of this class will be using.

            Attributes:
                    title (str): Title of the movie.
                    year (int): Production year of the movie.
                    storyline (str): Short story of the movie.
                    poster_image_url (str): Link of the movie's poster image.
                    trailer_youtube_url (str) : Link of the movie's trailer.
    """

    def __init__(self, title, year, storyline, poster_image_url,
                 trailer_youtube_url):

        self.title = title
        self.year = year
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
