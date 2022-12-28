
movies = [{"title": "Avengers", "director": "Steve Rogers", "year": "2010"},
          {"title": "Iron Man", "director": "Robert Downey Jr", "year": "2008"},
          {"title": "Thor", "director": "Chris Hemworth", "year": "2012"}]

# for i in range(0, len(movies)):
#
#     title = movies[i]["title"]
#     director = movies[i]["director"]
#     year = movies[i]["year"]
#     search_movie = input(f'enter title for the movie you are looking for: ')
#     if search_movie == title:
#         print(f"""your movie {title} was found and was directed by {director} in {year}""")
#         pass

######listing all movies###########
for i in range(0, len(movies)):
    # print(f'Movie title {movies[i]}, director {movies[i]}, and year {movies[i]} \n')
    print(f'Movie title {movies[i]}')


######finding movies###############
# res = None
# search_title = input("Enter the title for your movie: ")
# for movie in movies:
#     if movie['title'] == search_title:
#         res = movie
#         break
# print("The title was found: " + str(res))
def find_title_in_movielist(title, movies):
    return [element for element in movies if element['title'] == title]

print(find_title_in_movielist())