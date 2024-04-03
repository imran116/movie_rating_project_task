from django.urls import path
from . import views

app_name = 'loginApp'
urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sing_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
