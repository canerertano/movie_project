import json
import media
import fresh_tomatoes

# open the file which movies's information stored in.
file_stream = open("movie_db.json", "r")

# read the file and parse into json object.
json_data = json.loads(file_stream.read())

# get the movie list as json object.
movies_json = json_data["movies"]

# convert plain json to Movie class instances and add into movie list.
movies = []
for movie_json in movies_json:
    movies.append(media.Movie(movie_json["title"], movie_json["year"], movie_json["storyline"], movie_json["poster_image_url"],
                              movie_json["trailer_youtube_url"]))

# call the function that generates web page and pass the list of movies
fresh_tomatoes.open_movies_page(movies)
