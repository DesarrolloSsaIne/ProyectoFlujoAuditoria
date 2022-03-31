from django.urls import path
from apps.registration.views import login, logout



app_name = 'registration'
urlpatterns = [

    path('login/', login, name="login"),
    path(r'logout/', logout, name="logout"),


]