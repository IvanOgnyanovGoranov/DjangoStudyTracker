from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string


def manage_subjects(request):
    return HttpResponse("Here will be the subjects displayed!")


def edit_subject(request, pk):
    """Edits an existing subject."""
    pass


def delete_subject(request, pk):
    """Deletes a subject from the database."""
    pass


def add_subject(request):
    """User chooses what subject to add."""
    return HttpResponse("User chooses what subject to add.")



def redirect_to_view_stats(request):
    """Redirects to the stats view."""
    return HttpResponseRedirect(reverse('view_stats'))


