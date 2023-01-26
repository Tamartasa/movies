import datetime
import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

django.setup()

from movies_app.models import Movie, Rating

# new_movie = Movie(movie_name="aaa", release_year=2020, duration_in_min=124)
# new_movie.save()
# new_movie = Movie(movie_name="bbb", release_year=2022, duration_in_min=90)
# new_movie.save()
# new_movie = Movie(movie_name="ccc", release_year=2021, duration_in_min=101)
# new_movie.save()

all_movies = Movie.objects.all()
print(all_movies)
#
# for movie in all_movies:
#     Rating(movie=movie, rating=9, rating_date=datetime.datetime.now()).save()

movie = Movie.objects.get(pk=3)
print(movie.rating_set.all())