def greet():
    name = input("Enter your name: ")
    #print(f'Hello, {name}')
    return name

movies = []


def movie():
    title = input("enter title: ")
    director = input("enter director: ")
    year = input("entr year of movie: ")
    return title, director, year

print(movie())