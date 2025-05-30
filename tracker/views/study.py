from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string


def start_studying(request):
    """User picks a study subject and is redirected to the timer."""
    return HttpResponse("Here will be where user picks a subject and is redirected to the timer!")


def redirect_if_no_subject(request):
    """User clicks on Add to add a subject and is redirected to add_subject"""
    return HttpResponseRedirect(reverse('add_subject'))


def show_timer(request):
    return render(request, 'timer.html')

def add_study_time(request):
    return HttpResponse("User adds the study time to the correspondent subject")

