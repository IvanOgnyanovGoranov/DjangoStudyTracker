from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from tracker.models import Subject
from django.urls import reverse


# Create your views here.


def main_menu(request):
    url1 = reverse('manage_subjects')
    url2 = reverse('show_timer')
    url3 = reverse('view_stats')

    main_manu_options = (f'<ul>'
                         f'<li><a href="{url1}">Manage Subjects</a></li>'
                         f'<li><a href="{url2}">Start Timer</a></li>'
                         f'<li><a href="{url3}">View Stats</a></li>'
                         f'</ul>')
    return HttpResponse(main_manu_options)


def manage_subjects(request):
    return HttpResponse("Here will be the subjects!")


def show_timer(request):
    return HttpResponse("Here will be the timer!")


def view_stats(request):
    return HttpResponse("Here will be the stats!")

def main_menu_redirecting_numbers(response, number):
    valid_numbers = [1, 2, 3]

    if number not in valid_numbers:
        return HttpResponse('This number is not valid')

    # to be finished





