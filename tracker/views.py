from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from tracker.models import Subject
from django.urls import reverse

# Create your views here.


def pick_subject(request):
    response = ''
    subjects = Subject.objects.values_list('name', flat=True)

    for subject in subjects:
        url = reverse('subject_info', args=[subject])
        response += f'<li><a href="{url}">{subject.capitalize()}</a></li>'

    full_data = f'<ul>{response}</ul>'
    return HttpResponse(full_data)


def show_timer(request):
    return HttpResponse("Here will be the timer!")

def show_subject_info(request, subject):
    if Subject.objects.filter(name=subject).exists():
        return HttpResponse(f"Here will be the {subject}'s progress!")
    return HttpResponseNotFound('Subject not found!')


# If the user enters a URL as a number instead of name of subject,
# we redirect to the appropriate subject.
def subject_as_number(request, subject_number):
    """Redirects the user to the appropriate subject"""
    try:
        subject = Subject.objects.get(id=subject_number)
        redirect_path = reverse('subject_info', args=[subject.name])
        return HttpResponseRedirect(redirect_path)
    except Subject.DoesNotExist:
        return HttpResponseNotFound('Subject not found!')

