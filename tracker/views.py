from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse


# Create your views here.
MENU_ITEMS = [
    ('manage_subjects', 'Manage Subjects'),
    ('show_timer',     'Start Timer'),
    ('view_stats',     'View Stats'),
]

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

#to fix in the traker\urls
def main_menu_redirecting_numbers(request, menu_number):
    max_choice = len(MENU_ITEMS)
    if not (1 <= menu_number <= max_choice):
        return HttpResponseNotFound('This number is out of range!')

    view_name, _ = MENU_ITEMS[menu_number - 1]
    url = reverse(view_name)
    return HttpResponseRedirect(url)





