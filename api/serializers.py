from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from loginApp.models import UserProfile
from movieRatingApp.models import AddMovie, RateMovie


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'phone', 'password', 'email')


class AddMovieSerializer(ModelSerializer):
    class Meta:
        model = AddMovie
        fields = ('id', 'name', 'genre', 'rating', 'release_date')


class RateMovieSerializer(ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(source='movie', read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = RateMovie
        fields = ('id', 'user_id', 'movie_id', 'rating')

    def get_rating(self, obj):
        movie = obj.movie
        return round(movie.average_rating(), 1)

    # if movie.average_rating() is not None else None
