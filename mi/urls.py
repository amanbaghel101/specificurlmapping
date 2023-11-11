from mi.views import *
from django.urls import path
app_name = 'anyname'

urlpatterns = [
    path('rohit/', rohit,name='rohit')
]