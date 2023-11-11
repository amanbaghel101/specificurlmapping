from django.shortcuts import render
from django.contrib import admin
from django.urls import path

# Create your views here.
def msd(request):
    return render(request,'msd.html')
