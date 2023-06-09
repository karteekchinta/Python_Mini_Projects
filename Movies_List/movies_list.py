MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({'title': title, 'director': director, 'year': year})


#   - listing movies
def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


#   - finding movies
def find_movies():
    search_title = input("enter the movie you want to search")
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


def user_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            show_movies()
        elif selection == "f":
            find_movies()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


user_menu()