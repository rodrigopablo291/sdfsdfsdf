
from django.urls import path
from .views import *
from django.urls import path,
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name='index'),
    path('login_ingresar',login_ingresar,name='login_ingresar'),
    path('Match/',login_required(MatchListView.as_view()), name = 'Match_list'),
    
    
] 

