from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('users/', views.getUser),
    path('movies/', views.getMovies),
    path('ratings/', views.getRatings),
    path('ratings/<str:extra_param>', views.handle_invalid_api_request),
]

