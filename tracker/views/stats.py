from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string

def view_stats(request):
    return HttpResponse("Here will be general overview of all subject stats!")


def specific_subject_stats(request, pk):
    subject = Subject.objects.get(pk=pk)
    return HttpResponse("Here will be a detailed overview of the specific subject!")




