from rcb.views import *
from django.urls import path
app_name = 'anyname'

urlpatterns = [
    path('virat/', virat,name='virat')
]
