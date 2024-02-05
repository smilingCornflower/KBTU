from data import movies

# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
# Write a function that returns a sublist of movies with an IMDB score above 5.5.
# Write a function that takes a category name and returns just those movies under that category.
# Write a function that takes a list of movies and computes the average IMDB score.
# Write a function that takes a category and computes the average IMDB score.

def is_good_movie(movie_name):
    for mov in movies:
        if mov['name'] == movie_name:
            if mov['imdb'] > 5.5:
                return True
            else:
                return False
    "The movie is not on the list"


def get_good_movies(rating=5.5):
    result = []
    for mov in movies:
        if mov['imdb'] > rating:
            result.append(mov['name'])
    if not result:
        return "No good movies"
    return result


def get_movies_by_category(mov_category):
    result = []
    for mov in movies:
        if mov['category'] == mov_category:
            result.append(mov['name'])
    if not result:
        return f"No {mov_category} movies"
    return result


def calc_avarage(films):
    scores = []
    for mov in movies:
        if mov['name'] in films:
            scores.append(mov['imdb'])
    return sum(scores) / len(scores)


def calc_avarage_of_category(category):
    films = [i['name'] for i in movies if i['category'] == category]
    return calc_avarage(films)



print(is_good_movie('We Two'))      # True
print(is_good_movie('AlphaJet'))    # False
print()

print('Good movies list:')
print(*get_good_movies(), sep='\n')
print()

category = 'Romance'
print(f"{category} movies: {', '.join(get_movies_by_category('Romance'))}")
print()


film_names = ['Colonia', 'Joking muck', 'We Two', 'Usual Suspects']
print(f"The average rate of films is {calc_avarage(film_names)}")
print()

print(f"The avarage rate of {category} movies is {calc_avarage_of_category(category)}")