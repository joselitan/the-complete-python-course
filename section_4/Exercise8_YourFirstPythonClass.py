class Movie:
    def __init__(self, movie_name, movie_director):
        self.name = movie_name
        self.director = movie_director


my_movie = Movie('The Matrix', 'Wachowski')
print(my_movie.name, my_movie.director)
