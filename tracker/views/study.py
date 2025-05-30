from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string


def start_studying(request):
    """User picks a study subject and is redirected to the timer."""
    subjects = Subject.objects.all()
    return render(request, 'study/pick.html', {'subjects': subjects})


def redirect_if_no_subject(request):
    """User clicks on Add to add a subject and is redirected to add_subject"""
    return HttpResponseRedirect(reverse('add_subject'))


def show_timer(request, pk):
    """Shows the timer with the specific subject the user chose."""
    try:
        subject = Subject.objects.get(pk=pk)
        return render(request, 'study/timer.html',
                      {'subject': subject.name
                       }
                      )
    except Subject.DoesNotExist:
        return HttpResponseNotFound('Subject does not exist')


def add_study_time(request):
    return HttpResponse("User adds the study time to the correspondent subject")

