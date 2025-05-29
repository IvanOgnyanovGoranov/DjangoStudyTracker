from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string


def manage_subjects(request):
    return HttpResponse("Here will be the subjects displayed!")

# No paths created for the below
def edit_subject(request, pk):
    """Edits an existing subject."""
    pass


def delete_subject(request, pk):
    """Deletes a subject from the database."""
    pass


def add_subject(request, pk):
    """Adds a subject to the database."""
    pass


def view_subject_stats(request, pk):
    """Redirects to the stats view."""
    pass


