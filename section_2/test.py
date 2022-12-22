friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

#for name in friend_ages.values():
#    #print(f'my friends name is {name} and is {age} years old')
#    print(f'age of friend: {name}')

for name, age in friend_ages.items():
    #print(f'my friends name is {name} and is {age} years old')
    #print(f'{name} is {age} years old.'
    pass

movies = [{"title": "Avengers", "director": "Steve Rogers", "year": "2010"},
          {"title": "Iron Man", "director": "Robert Downey Jr", "year": "2008"},
          {"title": "Thor", "director": "Chris Hemworth", "year": "2012"}]

for i in range(0, len(movies)):

    title = movies[i]["title"]
    director = movies[i]["director"]
    year = movies[i]["year"]
    search_movie = input(f'enter title for the movie you are looking for: ')
    if search_movie == title:
        print(f"""your movie {title} was found and was directed by {director} in {year}""")
        pass

for movie in movies:
    print(movie)
#print(movies)