from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddMovieForm
from movieRatingApp.models import AddMovie, RateMovie
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def index_view(request):
    movies = AddMovie.objects.all()[:4]
    return render(request, 'movieRatingApp/index.html', context={'movies':movies})


@login_required
def home_view(request):
    movies = AddMovie.objects.all()
    return render(request, 'movieRatingApp/home.html', context={'movies': movies})


@login_required
def add_movie_view(request):
    form = AddMovieForm()
    if request.method == 'POST':
        form = AddMovieForm(data=request.POST)
        if form.is_valid():
            movie_instance = form.save(commit=False)
            movie_instance.user = request.user
            movie_instance.save()
            messages.success(request, "Your movie added successfully.")
            return redirect('movieRatingApp:add-movie')

    return render(request, 'movieRatingApp/add_movie.html', context={'form': form})


@login_required
def rate_movie_view(request, pk):
    if request.method == 'POST':
        rate = request.POST.get('rating')
        if rate:
            movie = AddMovie.objects.get(pk=pk)
            rate_movie = RateMovie.objects.create(user=request.user, movie=movie, rating=rate)
            rate_movie.save()
            messages.success(request, "Your Ratings Submitted.Thank You!")
            return redirect('movieRatingApp:home')
        else:
            messages.warning(request, "Please select a rating.")

    return render(request, 'movieRatingApp/rate_movie.html', context={'movies': AddMovie.objects.get(pk=pk)})


@login_required
def movie_detail_view(request, pk):
    movie = AddMovie.objects.get(pk=pk)
    return render(request, 'movieRatingApp/detail_movie.html', context={'movie': movie})


@login_required
def search_movie_view(request):
    query = request.GET.get('movie_search')
    movies = None

    if query:
        movies = AddMovie.objects.filter(Q(name__icontains=query) | Q(genre__icontains=query))
        if not movies.exists():
            messages.info(request, f"No movies found for '{query}'.")
    else:
        messages.warning(request, "Search box is empty. Please enter a keyword.")
        return redirect('movieRatingApp:home')

    return render(request, "movieRatingApp/search_movie.html", context={'movies': movies, 'query': query})