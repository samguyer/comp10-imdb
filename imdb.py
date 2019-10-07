
# -- Here are the seven functions you need to implement

# -- Find a movie by title
#    Given a movie title (string) and a list of movies, find that movie in the
#    list (if it is there), and print out all of the information about it.
#    Bonus: print out a message if the given title is NOT in the list
def find_movie_by_title(title, movies):
    print("Not yet implemented")

# -- List movies by year
#    Given a year (int) and a list of movies, print out the titles of the movies
#    made in that year
def movies_by_year(year, movies):
    print("Not yet implemented")

# -- Average movie box office gross
#    Given a list of movies, compute the average amount of money in ticket sales
#    made by any movie in the list
def average_gross(movies):
    print("Not yet implemented")

# -- Highest and lowest grossing movies
#    Given a list of movies, print the titles of the movie that made the most
#    money and the movie that made the least money
def best_worst_movies(movies):
    print("Not yet implemented")

# -- Actor filmography
#    Given an actor name (string) and a list of movies, print the titles of all
#    movies in which that actor appeared
def actor_filmography(actor, movies):
    print("Not yet implemented")

# -- Movie gross in a year
#    Given a year and a list of movies, print the total amount of money made by
#    all the movies in that year together
def year_gross(year, movies):
    print("Not yet implemented")

# -- Best year
#    Given a list of movies, determine which year had the highest total money
#    made for all movies in that year.
def best_year(movies):
    print("Not yet implemented")

# ----------------------------------------------------------------------------
#    You should not need to change any of the code below, but take a look
#    at it to make sure understand what it does...

# -- This function reads the data from a file and stores it in the list of
#    tuples data structure
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
filename = input('Enter IMDB file name: ')
movies = read_movie_file((filename))
# print(movies)

done = False
while not done:
    print('Choose a query...')
    print('1: Find a movie by title')
    print('2: List movies made in a given year')
    print('3: Compute average box office gross')
    print('4: Find highest and lowest grossing movies')
    print('5: Find all the movies with a given actor')
    print('6: Compute total box office gross for a given year')
    print('7: Find the highest grossing year')
    s = input('Enter 1-7 (any other number to quit): ')

    choice = int(s)
    if choice == 1:
        t = input('Enter a title: ')
        find_movie_by_title(t, movies)
    elif choice == 2:
        y = input('Enter a year: ')
        year = int(y)
        movies_by_year(year, movies)
    elif choice == 3:
        average_gross(movies)
    elif choice == 4:
        best_worst_movies(movies)
    elif choice == 5:
        actor = input('Enter actor name: ')
        actor_filmography(actor, movies)
    elif choice == 6:
        y = input('Enter a year: ')
        year = int(y)
        year_gross(year, movies)
    elif choice == 7:
        best_year(movies)
    else:
        done = True

