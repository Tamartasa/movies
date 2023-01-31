import datetime
import os
import django
from django.db.models import Q, Count, Min, Max, Avg

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

django.setup()

from movies_app.models import *


def get_youngest_50() -> list[Actor]:
    """
    get all the actors in the db who are younger than 50 years old
    :return:
    """
    actors = Actor.objects.filter(birth_year__gt=(datetime.datetime.now().year - 50))
    return list(actors)


def get_movies_after2005() -> list[Movie]:
    """
    Get movies that last less than 2.5 hours and were released after 2005
    :return:
    """
    movies = Movie.objects.filter(release_year__gt=2005, duration_in_min__lt=150)
    return list(movies)


def get_movies_contains_words(release_before_2010=False) -> list[Movie]:
    """
    Get all the movies that contain a word “criminal”, “mob” or “cop” in their description
    if True - get only movies that were released before 2010
    :return:
    """
    if release_before_2010:
        return list(Movie.objects.filter(Q(release_year__lt=2010, description__contains='criminal') | Q(description__contains='mob') |
                                         Q(description__contains='cop')))
    return list(Movie.objects.filter(Q(description__contains='criminal') | Q(description__contains='mob') |
                             Q(description__contains='cop')))


def actors_and_movies() ->list[dict[str: str]]:
    """
    Get list of actors, and add amount of movies they played in (for each one)
    :return:
    """
    ret_val = Actor.objects.values('name').annotate(movies_count=Count('movieactor__movie_id'))
    return list(ret_val)

def min_max_avg_rating():
    """
    Get average, min, and max rating in the system
    :return:
    """
    mma = Rating.objects.aggregate(min_rating=Min('rating'), max_rating=Max('rating'), avg_rating=Avg('rating'))
    return mma


def get_movies_and_avg_rating():
    """
    Get Movies with their avg ratings
    :return:
    """
    ret_val = Movie.objects.values('movie_name').annotate(avg_rating=Avg('rating__rating'))
    ret_val = list(ret_val)

    for r in ret_val:
        print(r)

def rating_2023() -> list[Rating]:
    """
    Get ratings that were created in 2023
    :return:
    """
    print(Rating.objects.filter(rating_date__year=2023))

def rating_actors():
    """
    Get all the actors in the system with min and max rating of the movies they played in
    :return:
    """
    actors = Actor.objects.values('name').annotate(min_rating=Min('movieactor__movie_id__rating__rating'),
                                                   max_rating=Max('movieactor__movie_id__rating__rating'))
    print(actors)
    for a in actors:
        print(f"Actor: {a['name']} -- min rating: {a['min_rating']} | max rating: {a['max_rating']}")

def movies_avg_salary():
    """
    Get movies with average salary for actors in each one
    :return:
    """
    m = Movie.objects.values('movie_name').annotate(avg_salary=Avg('movieactor__salary'))
    for movie in m:
        print(f"{movie['movie_name']} -- avg salary: {movie['avg_salary']}")

def actors_avg_salary():
    """
    Get actors with their average salaries
    :return:
    """
    actors = Actor.objects.values('name').annotate(avg_salary=Avg('movieactor__salary'))
    for a in actors:
        print(f"{a['name']} -- avg salary: {a['avg_salary']}")

def main_roles() -> list[Actor]:
    """
    Get actors who played main roles at least once
    :return:
    """
    print(Actor.objects.filter(movieactor__main_role=True))

def movies_actors_main_roles():
    """
    Get movies and amount of actors who played main roles
    :return:
    """
    print(Movie.objects.values('movie_name').annotate(main_roles=Count('movieactor__main_role')))

if __name__ == '__main__':

    # print(get_youngest_50())
    # print(get_movies_after2005())
    # print(get_movies_contains_words(release_before_2010=True))
    # print(get_movies_contains_words())
    # print(actors_and_movies())
    # print(min_max_avg_rating())
    # get_movies_and_avg_rating()
    # rating_2023()
    rating_actors()
    # movies_avg_salary()
    # actors_avg_salary()
    # main_roles()
    # movies_actors_main_roles()