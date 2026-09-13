#Ejercicio 5 - Movie Collection

class Movie:
    def __init__(self, title,director,duration):

        if duration<=0:
            raise ValueError("Your movie duratiobn must be grater than 0")

        
        self.title = title
        self.director = director
        self.duration = duration


class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self,new_movie):
        self.movies.append(new_movie)

    def show_movies(self):
        if len(self.movies) == 0:
            print("We have no data yet")
            return

        print("===MOVIE LIST===")

        for movie in self.movies:
            print(f"Title: {movie.title}")
            print(f"Director: {movie.director}")
            print(f"Duration: {movie.duration}")


    def total_movies(self):
        return len(self.movies)

    def longest_movie(self):
        if len(self.movies) == 0:
            print("There are no movies on the collection")
            return


        longest = self.movies[0] 

        for movie in self.movies:
            if movie.duration > longest.duration:
                longest = movie 


        print("==Longest Movie==")
        print(f"Title: {longest.title}")
        print(f"Director: {longest.director}")
        print(f"Duration: {longest.duration}")



#                                                               ===[Creacion del objeto]===



collection = MovieCollection()


#                                                               ==={MENU}===

def Menu():
    print("=={Welcome To the Menu!}==")

    print("1. Add a movie")
    print("2. Show movies")
    print("3. See the total of movies")
    print("4. See the longest movie") 
    print("5. Exit")



#                                                         ==={EJECUTABLE MENU}===

while True:
    Menu()
    option = input("Enter the desired option: ")

    if option == "1":
        title = input("Add the title of your movie: ")
        director = input("Add the name of the director of the movie: ")
        duration = float(input("Enter the duration of the movie: "))
        movie = Movie(title,director,duration)
        collection.add_movie(movie)

    elif option == "2":
        collection.show_movies()

    elif option =="3":
        collection.total_movies()
        print(f"Total movies: {collection.total_movies()}")


    elif option == "4":
        collection.longest_movie()

    else:
        print("Exiting the system. Bye Bye ")
        break




