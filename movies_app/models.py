from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Movie(models.Model):

    movie_name = models.CharField(db_column='movie_name', max_length=256, null=False)
    description = models.TextField(db_column='description', null=True)
    duration_in_min = models.FloatField(db_column='duration', null=False)
    release_year = models.IntegerField(db_column='year', null=False,
                                       validators=[MinValueValidator(1900), MaxValueValidator(2050)])
    pic_url = models.URLField(max_length=512, db_column='pic_url', null=True)

    # will give name to the table - we will create class in the class
    class Meta:
        db_table = 'movies'

class Rating(models.Model):

    movie = models.ForeignKey("Movie", on_delete=models.RESTRICT)
    rating = models.SmallIntegerField(db_column="rating", null=False,
                             validators=[MinValueValidator(0), MaxValueValidator(11)])
    rating_date = models.DateField(db_column="rating_date", null=False)

    class Meta:
        db_table = 'ratings'


class Review(models.Model):

    movie = models.ForeignKey("Movie", on_delete=models.RESTRICT)
    review_text = models.TextField(db_column="review_text", null=False)
    review_date = models.DateField(db_column="review_date", null=False)

    class Meta:
        db_table = 'reviews'