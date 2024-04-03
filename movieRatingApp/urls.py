from django.urls import path
from . import views

app_name = 'movieRatingApp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('home/', views.home_view, name='home'),
    path('add-movie/', views.add_movie_view, name='add-movie'),
    path('rate-movie/<str:pk>/', views.rate_movie_view, name='rate-movie'),
    path('detail-movie/<str:pk>/', views.movie_detail_view, name='detail-movie'),
    path('search-movie/', views.search_movie_view, name='search-movie'),
]

