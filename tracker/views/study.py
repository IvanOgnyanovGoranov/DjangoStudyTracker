from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string

def start_studying(request):
    return HttpResponse("Here will be where user picks a subject and is redirected to the timer!")


def show_timer(request):
    return render(request, 'timer.html')

