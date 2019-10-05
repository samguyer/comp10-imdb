
# -- Here are the six functions you need to implement

def movies_by_year(year, movies):
    print("Not yet implemented")

def average_gross(movies):
    print("Not yet implemented")

def best_worst_movies(movies):
    print("Not yet implemented")

def actor_filmography(actor, movies):
    print("Not yet implemented")

def year_gross(year, movies):
    print("Not yet implemented")

def best_year(movies):
    print("Not yet implemented")

# -- This function reads the data in from a file and stores
#    it in the list of tuples data structure
def read_movie_file(moviefile):
    # -- Open the file and read all the lines into a big list
    with open(moviefile) as f:
        lines = [line.rstrip() for line in f]

    # -- Each group of 9 lines gives us all the information about a movie
    movielist = []
    for i in range(0,len(lines), 9):
        title = lines[i]
        year = int(lines[i+1])
        gross = int(lines[i+2])
        director = lines[i+3]
        actors = lines[i+4:i+9]

        # -- Make a tuple with this information and add to the big list of movies
        movie = (title, year, gross, director, actors)
        movielist.append(movie)

    return movielist

# -- Here's where the program actually starts running...
filename = input('Enter IMDB file name:')
movies = read_movie_file((filename))
# print(movies)

done = False
while not done:
    print('Choose a query...')
    print('1: List movies made in a given year')
    print('2: Compute average box office gross')
    print('3: Find highest and lowest grossing movies')
    print('4: Find all the movies with a given actor')
    print('5: Compute total box office gross for a given year')
    print('6: Find the highest grossing year')
    s = input("Enter 1-6 (any other number to quit): ")

    choice = int(s)
    if choice == 1:
        y = input("Enter a year: ")
        year = int(y)
        movies_by_year(year, movies)
    elif choice == 2:
        average_gross(movies)
    elif choice == 3:
        best_worst_movies(movies)
    elif choice == 4:
        actor = input("Enter actor name: ")
        actor_filmography(actor, movies)
    elif choice == 5:
        y = input("Enter a year: ")
        year = int(y)
        year_gross(year, movies)
    elif choice == 6:
        best_year(movies)
    else:
        done = True

