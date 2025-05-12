from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_timer(request):
    return HttpResponse("Here will be the timer!")

def show_progress(request):
    return HttpResponse("Here will be the progress!")
