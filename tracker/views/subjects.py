from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string


def manage_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'manage_subjects/subject_manager.html', {'subjects': subjects})


def edit_or_delete_subject(request, pk):
    """Edits or deletes an existing subject."""
    # have to get the pk of the subject to redirect it to edit or delete this subject
    subject = get_object_or_404(Subject, pk=pk)
    return HttpResponse(f"Here will be the edit or delete displayed for {subject.name}!")


def add_subject(request):
    """User chooses what subject to add."""
    return HttpResponse("User chooses what subject to add.")


def redirect_to_view_stats(request):
    """Redirects to the stats view."""
    return HttpResponseRedirect(reverse('view_stats'))


