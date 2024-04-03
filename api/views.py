from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from loginApp.models import UserProfile
from movieRatingApp.models import AddMovie, RateMovie
from .serializers import UserSerializer, AddMovieSerializer, RateMovieSerializer



@api_view(['GET'])
def getRoutes(request):
    routes = [

        'GET/api',
        'GET/api/users',
        'GET/api/movies',
        'GET/api/ratings',
    ]
    return Response(routes)


@api_view(['GET'])
def getUser(request):
    user = UserProfile.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMovies(request):
    movies = AddMovie.objects.all()
    serializer = AddMovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRatings(request):
    ratings = RateMovie.objects.all()
    serializer = RateMovieSerializer(ratings, many=True)
    return Response(serializer.data)


def handle_invalid_api_request(request,extra_param):
    return JsonResponse({'error': 'Invalid API request','valid':'for find routes use /api'}, status=400)