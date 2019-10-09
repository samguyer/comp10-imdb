
# -- Here are the seven functions you need to implement

# -- Find a movie by title
#    Given a movie title (string) and a list of movies, find that movie in the
#    list (if it is there). Return the full tuple, or None if not found.
def find_movie_by_title(title, movies):
    print("Not yet implemented")
    return None

# -- List movies by year
#    Given a year (int) and a list of movies, return a list of movies made in
#    that year.
def movies_by_year(year, movies):
    print("Not yet implemented")
    return None

# -- Average movie box office gross
#    Given a list of movies, compute the average amount of money in ticket sales
#    made by any movie in the list
def average_gross(movies):
    print("Not yet implemented")
    return 0

# -- Highest grossing movie
#    Given a list of movies, return the movie that made the most money of
#    all the movies in the list
def best_movie(movies):
    print("Not yet implemented")
    return None

# -- Highest grossing movie
#    Given a list of movies, return the movie that made the least money of
#    all the movies in the list
def worst_movie(movies):
    print("Not yet implemented")
    return None

# -- Actor filmography
#    Given an actor name (string) and a list of movies, return the list of
#    all movies in which that actor appears
def actor_filmography(actor, movies):
    print("Not yet implemented")
    return None

# -- Movie gross in a year
#    Given a year and a list of movies, return the total amount of money made by
#    all the movies in that year together
def year_gross(year, movies):
    print("Not yet implemented")
    return 0

# -- Best year
#    Given a list of movies, determine which year had the highest total money
#    made for all movies in that year.
def best_year(movies):
    print("Not yet implemented")
    return 1900

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
    print('4: Find highest grossing movie')
    print('5: Find lowest grossing movie')
    print('6: Find all the movies with a given actor')
    print('7: Compute total box office gross for a given year')
    print('8: Find the highest grossing year')
    s = input('Enter 1-8 (any other number to quit): ')

    choice = int(s)
    if choice == 1:
        t = input('Enter a title: ')
        m = find_movie_by_title(t, movies)
        print(m)
    elif choice == 2:
        y = input('Enter a year: ')
        year = int(y)
        result = movies_by_year(year, movies)
        print(result)
    elif choice == 3:
        g = average_gross(movies)
        print("Average gross is $" + str(g))
    elif choice == 4:
        m = best_movie(movies)
        print(m)
    elif choice == 5:
        worst_movie(movies)
        print(m)
    elif choice == 6:
        actor = input('Enter actor name: ')
        result = actor_filmography(actor, movies)
        print(result)
    elif choice == 7:
        y = input('Enter a year: ')
        year = int(y)
        g = year_gross(year, movies)
        print("Total gross is $" + str(g))
    elif choice == 8:
        y = best_year(movies)
        print(y)
    else:
        done = True

