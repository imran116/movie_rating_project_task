from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your models here.

class AddMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='add_movie_user')
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    release_date = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def average_rating(self):
        return RateMovie.objects.filter(movie=self).aggregate(avg_rating=Avg('rating'))['avg_rating']


class RateMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(AddMovie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3,decimal_places=1,default=0.0)
