from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import  InicioDashboard
from django.conf.urls import url, include
urlpatterns = [

 path(r'', login_required(InicioDashboard.as_view()), name="dashboard"),

]
