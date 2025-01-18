import json

class MovieLibrary:
    """Exception for when a movie is not found """
    
    class MovieNotFoundError(Exception):
        pass
    def __init__(self, json_file=None):
        if json_file is None:
            json_file = r'C:\Users\laman\Desktop\School\Programming principles\Programming Principles - Traccia (1)\movies.json'
        self.json_file = json_file
        try: 
            with open(json_file, "r") as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.json_file}")
        
    def get_movies(self):
        """Return a list of all movies"""
        return self.movies
    
    def add_movie(self, title, director, year, genres):
        """Adds a new movie and updates the json file"""
        new_movie = {
            'title': title,
            'director': director,
            'year': year,
            'genre': genres
        }
        self.movies.append(new_movie)
        self.update_json_file()
        
    def remove_movie(self, title):
        """Removes a chosen movie by title and updates the JSON file """
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                self.update_json_file()
                return movie
        raise self.MovieNotFoundError("Movie not found")
        
    def update_json_file(self):
        """Updates JSON file"""
        with open(self.json_file, 'w') as file: 
            json.dump(self.movies, file, indent=4)
            
    def get_movie_titles(self):
        """Returns a list of all movie titles in the JSON file """
        return [movie['title'] for movie in self.movies]
    
    
    def count_movies(self):
        """Returns the movie count"""
        return len(self.movies)
    
    def get_movie_by_title(self, title):
        """Returns the movie by title"""
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie
        raise self.MovieNotFoundError("movie nt found")
    
    def get_movies_by_title_substring(self, substring): 
        """Returns all movies containing the specific substring provided"""
        return [movie for movie in self.movies if substring in movie['title']]
    
    def get_movies_by_year(self,year):
        """returns All movies released within a given year"""
        return [movie for movie in self.movies if movie['year']== year]
    
    def count_movies_by_director(self, director):
        """Returns a count of movies released by a specific director"""
        return sum (1 for movie in self.movies if movie['director'].lower() == director.lower() )
    
    
    def get_movies_by_genre(self,genre):
        """Returns a list of movies that have a specific genre"""
        return [movie for movie in self.movies if genre.lower() in (g.lower() for g in movie['genre'])]
    
    def get_oldest_movie_title(self):
        """Returns the oldest movie """
        oldest_movie = self.movies[0]
        
        for movie in self.movies: 
            if movie['year'] < oldest_movie['year']:
                oldest_movie = movie
        return oldest_movie["title"]
    
    def get_average_release_year(self): 
        """Returns the avg release year """
        return sum(movie['year'] for movie in self.movies) / len(self.movies)
    
    def get_longest_title(self):
        """Finds the movie with the longest title"""
        longest_title_movie = self.movies[0]
        
        for movie in self.movies:
            if len(movie['title']) > len(longest_title_movie["title"]):
                longest_title_movie = movie
        return longest_title_movie["title"]
    
    
    def get_titles_between_years(self, beg_year, end_year):
        """Returns the title of movies that are released between two given years"""
        return [movie["title"] for movie in self.movies if beg_year<= movie["year"] <= end_year]
    
    def get_most_common_year(self): 
        """Returns the year with the most movies made and ignores cases where there's a tie """
        year_counts = {}
        
        for movie in self.movies:
            year = movie['year']
            if year in year_counts:
                year_counts[year] += 1
            else:
                year_counts[year] = 1 
                
        return max(year_counts, key=year_counts.get)
        

# if __name__ == "__main__":
#     library = MovieLibrary(r'C:\Users\laman\Desktop\School\Programming principles\Programming Principles - Traccia (1)\movies.json')

# for movie in library.get_movies():
#     print(movie)

# print("most common year:", library.get_most_common_year())

# library.add_movie("Harry potter", "Alfonso", 2001, 'Sci-fi' )

# for movie in library.get_movies():
#     print(movie)

# print(library.get_longest_title())
# print(library.get_movie_titles())
# print(library.count_movies())


