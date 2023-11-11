from csk.views import *
from django.urls import path

app_name = 'anyname'

urlpatterns = [
    path('msd/',msd,name='msd')
]
